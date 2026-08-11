from .collectors.github import find_opportunities
def main():
    oppotunities = find_opportunities()
    print(f"Found {len(oppotunities)} opportunities.\n")

    for opportunity in oppotunities:
        print("=" * 60)
        print(opportunity.title)
        print(f"Source: {opportunity.source}")
        print(f"URL: {opportunity.url}")
        print()

if __name__ == "__main__":
    main()