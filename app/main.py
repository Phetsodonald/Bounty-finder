from app.collectors.github import find_opportunities


def main():
    opportunities = find_opportunities()

    print(f"Found {len(opportunities)} opportunities.\n")

    for opportunity in opportunities:
        print("=" * 60)
        print(opportunity.title)

        if opportunity.reward is not None:
            print(
                f"Reward: {opportunity.reward:g} "
                f"{opportunity.currency}"
            )
        else:
            print("Reward: Unknown")

        print(f"Source: {opportunity.source}")
        print(f"URL: {opportunity.url}")
        print()


if __name__ == "__main__":
    main()