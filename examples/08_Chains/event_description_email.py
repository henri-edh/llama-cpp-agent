# Example: Event Description and Invitation Email
from llama_cpp_agent.chain import AgentChainElement, AgentChain
from llama_cpp_agent.llm_agent import LlamaCppAgent
from llama_cpp_agent.messages_formatter import MessagesFormatterType
from llama_cpp_agent.providers.llama_cpp_endpoint_provider import LlamaCppEndpointSettings

model = LlamaCppEndpointSettings(completions_endpoint_url="http://127.0.0.1:8080/completion")

agent = LlamaCppAgent(
    model,
    debug_output=True,
    system_prompt="",
    predefined_messages_formatter_type=MessagesFormatterType.MIXTRAL
)

event_description = AgentChainElement(
    output_identifier="out_0",
    system_prompt="You are an event planner",
    prompt="Create a detailed description for a {event_type} event taking place on {event_date} at {event_venue}. Include key highlights and activities."
)

invitation_email = AgentChainElement(
    output_identifier="out_1",
    system_prompt="You are an email marketing specialist",
    prompt="Write an engaging invitation email based on the following event description. Include a clear call-to-action:\n--\n{out_0}"
)

chain = [event_description, invitation_email]
agent_chain = AgentChain(agent, chain)
agent_chain.run_chain(additional_fields={"event_type": "Conference", "event_date": "September 15-17, 2023", "event_venue": "Grand Hotel"})
