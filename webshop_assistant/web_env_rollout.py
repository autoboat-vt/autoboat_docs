
# TODO MAKE A CONVERSATION OBJECT FROM TRANSFORMERS TO HAVE A CONTINUOUS MULTITURN CONVERSATION

import gym
from web_agent_site.envs import WebAgentTextEnv
from utils import get_hugging_face_auth_token, get_action_from_response
from transformers import AutoProcessor, pipeline
import torch

TEMPERATURE = 0.7
REFLECTION_MODEL_INTERJECTION_RATE = 5  # the number of steps between the time that the reflection model speaks

ACTOR_MODEL_NAME = "google/gemma-3-12b-it"
# ACTOR_MODEL_NAME = "google/gemma-3-12b-it"
# REFLECTION_MODEL_NAME = "google/gemma-3-4b-it"
# REFLECTION_MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
REFLECTION_MODEL_NAME = "google/gemma-3-1b-it"


ACTOR_SYSTEM_PROMPT = "You are a web shopping assistant. Your job is to interact with a \
web page by clicking on buttons or searching for the product in a search bar in the web page. \
At every step in the process, you will receive whether a search bar is in the current web page, \
and if it is, you can output 'search[<ENTER YOUR SEARCH QUERY HERE>]' to use the search bar. \
If you would like to click a button in the available buttons, please output 'click[<ENTER THE NAME OF THE BUTTON TO CLICK HERE>]'. \
For example, if there is a button named 'next page' and you would like to click it, please respond with click[next page]. \
If you would like to search for shoes, please respoond with search[shoes]. Please think about the correct action to perform \
and then perform either the 'click' or 'search' action at the very end of your response. \
Your goal is to find the product that is listed by using the given commands, but you may only use one of the given commands at a time. \
Ocassionally, you will be given feedback on your performance that will be in the form of <Feedback> YOUR FEEDBACK WILL BE HERE <\\Feedback> \
Please remember that the product always exists on the webpage. You cannot give up under any circumstance, but you can try relaxing the search criteria slightly \
to get to the best match to the prompt. If you are absolutely unable to find any similar items please output click[done]"


REFLECTION_SYSTEM_PROMPT = "You are a supervisor for a web shopping assistant LLM. Your job is to instruct the \
web shopping assistant whether you believe that they are on the right track, and if they are not on the right track, \
then you should inform the web shopping assistant what it is doing wrong and what it should do instead. \
You will be given the web shopping assistant's long term task and their current action"


HUGGING_FACE_AUTH_TOKEN = get_hugging_face_auth_token("hugging_face_auth_token.txt")
actor_model_pipeline = pipeline("text-generation", model=ACTOR_MODEL_NAME, device="cuda", torch_dtype=torch.bfloat16)
reflection_model_pipeline = pipeline("text-generation", model=REFLECTION_MODEL_NAME, device="cuda", torch_dtype=torch.bfloat16)

reflection_model_context = [{"role": "system", "content": REFLECTION_SYSTEM_PROMPT},] # https://huggingface.co/docs/transformers/en/conversations
actor_model_context = [{"role": "system", "content": ACTOR_SYSTEM_PROMPT},]


env = gym.make('WebAgentTextEnv-v0', observation_mode='text', num_products=1000)
obs, info = env.reset()
obs, info = env.reset()
obs, info = env.reset()
obs, info = env.reset()
obs, info = env.reset()
done = False

reflection_model_observation = ""
actor_model_observation = ""


index = 0
while not done: 
    actor_model_observation = obs + f". Buttons that you can click with click[Button to Click]: {env.get_available_actions()['clickables']}. Can you use the search bar with search[Search Query]: {env.get_available_actions()['has_search_bar']}."

    if (index % REFLECTION_MODEL_INTERJECTION_RATE == 0 and index != 0):
        reflection_model_context.append({"role": "user", "content": reflection_model_observation})
        reflection_model_observation = ""

        reflection_model_context = reflection_model_pipeline(text_inputs=reflection_model_context)[0]["generated_text"]
        print(reflection_model_context[-1]["content"])
        actor_model_observation += "<Feedback>" + reflection_model_context[-1]["content"] + r"<\Feedback>"


    actor_model_context.append({"role": "user", "content": actor_model_observation})
    actor_model_context = actor_model_pipeline(text_inputs=actor_model_context)[0]["generated_text"]    
    action = get_action_from_response(actor_model_context[-1]["content"])

    if action == "click[done]":
        done = True
        break

    print(actor_model_context[-1]["content"])


    reflection_model_observation += "<Shopping Assistant Task>" + obs + r"<\Shopping Assistant Task> "
    reflection_model_observation += "<Shopping Assistant Action>" + action + r"<\Shopping Assistant Action>"

    obs, reward, done, info = env.step(action)

    index+=1