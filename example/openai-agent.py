from agents import Agent, Runner
import asyncio


english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
)

async def main():
    result = await Runner.run(english_agent, input="Hey how are you?")
    print(result.final_output)
    # ¡Hola! Estoy bien, gracias por preguntar. ¿Y tú, cómo estás?


if __name__ == "__main__":
    asyncio.run(main())