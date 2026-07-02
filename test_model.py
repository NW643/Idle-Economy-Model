from model import SimulationConfig, simulateFixedCost


def main() -> None:
    """
    Run a basic test of the fixed-cost idle economy model.

    This is not a formal unit test yet.
    It is just a quick script to check that the simulation runs and prints useful output.
    """

    # Create a test configuration.
    config = SimulationConfig(
        startingBalance=0.0,
        startingProducers=1,
        producerCost=10.0,
        incomePerProducer=1.0,
        simulationDuration=60.0,
        maxEvents=10_000,
    )

    # Run the simulation.
    rows = simulateFixedCost(config)

    # Print the first few events so we can inspect the early behaviour.
    print("First 10 events:")
    for row in rows[:10]:
        print(row)

    # Print the last few events so we can inspect the final behaviour.
    print("\nLast 5 events:")
    for row in rows[-5:]:
        print(row)

    # Store the final row for summary stats.
    finalRow = rows[-1]

    # Print a readable summary.
    print("\nSummary:")
    print(f"Total rows recorded: {len(rows)}")
    print(f"Final event: {finalRow['event']}")
    print(f"Final time: {finalRow['time']}")
    print(f"Final balance: {finalRow['balance']}")
    print(f"Final producers: {finalRow['producers']}")
    print(f"Final income per second: {finalRow['incomePerSecond']}")
    print(f"Total earned: {finalRow['totalEarned']}")


if __name__ == "__main__":
    main()