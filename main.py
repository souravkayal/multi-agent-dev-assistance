from agents.main_agent import get_main_agent


def main():
    agent = get_main_agent()
    print("Multi-Agent System Ready. Type your query.")
    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.run(user_input)
        print(response)


if __name__ == "__main__":
    main()
