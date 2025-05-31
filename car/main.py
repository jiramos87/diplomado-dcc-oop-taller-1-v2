from car import Car

def print_gas_status(car, operation):
    """Helper function to print gas consumption after each operation"""
    print(f"   → Gas consumption after {operation}: {car.get_gas_consumption()}")

def main():
    # Create a new car instance
    car = Car()
    
    print("=" * 60)
    print("TESTING CAR OPERATIONS WITH GAS CONSUMPTION")
    print("=" * 60)
    
    # Show initial gas consumption
    print(f"\nInitial gas consumption: {car.get_gas_consumption()}")
    
    # Test different operations in various orders
    print("\n" + "="*40)
    print("BASIC OPERATIONS TEST")
    print("="*40)
    
    print("\n1. Trying to accelerate while off (should not consume gas):")
    car.accelerate()
    print_gas_status(car, "accelerating while off")
    
    print("\n2. Turning on the car (should consume 30):")
    car.turn_on()
    print_gas_status(car, "turning on")
    
    print("\n3. Accelerating while on (should consume 10):")
    car.accelerate()
    print_gas_status(car, "accelerating while on")
    
    print("\n4. Braking while on (should not consume gas):")
    car.brake()
    print_gas_status(car, "braking")
    
    print("\n5. Trying to turn on while already on (should not consume gas):")
    car.turn_on()
    print_gas_status(car, "trying to turn on while on")
    
    print("\n6. Multiple accelerations to test consistent consumption:")
    for i in range(3):
        print(f"   Acceleration {i+1}:")
        car.accelerate()
        print_gas_status(car, f"acceleration {i+1}")
    
    print("\n7. Turning off the car (should not consume gas):")
    car.turn_off()
    print_gas_status(car, "turning off")
    
    print("\n8. Trying to brake while off (should not consume gas):")
    car.brake()
    print_gas_status(car, "braking while off")
    
    # Test overheating scenario
    print("\n" + "="*40)
    print("OVERHEATING TEST")
    print("="*40)
    
    print(f"\nCurrent gas consumption: {car.get_gas_consumption()}")
    print("\n9. Starting fresh for overheating test:")
    car.turn_on()  # Consume 30
    print_gas_status(car, "turning on for overheating test")
    
    print("\n10. Accelerating 5 times to trigger overheating:")
    for i in range(5):
        print(f"   Acceleration {i+1}/5:")
        car.accelerate()
        print_gas_status(car, f"acceleration {i+1}/5")
        if i == 4:  # After 5th acceleration, should be overheated
            print("   *** OVERHEATING SHOULD HAVE OCCURRED (+50 gas) ***")
    
    print("\n11. Trying to accelerate while overheated (should consume 20):")
    car.accelerate()
    print_gas_status(car, "accelerating while overheated")
    
    print("\n12. Trying to turn off while overheated (should not consume gas):")
    car.turn_off()
    print_gas_status(car, "trying to turn off while overheated")
    
    print("\n13. Trying to brake while overheated (should not consume gas):")
    car.brake()
    print_gas_status(car, "braking while overheated")
    
    print("\n14. Another acceleration while overheated (should consume 20 more):")
    car.accelerate()
    print_gas_status(car, "second acceleration while overheated")
    
    print("\n15. Cooling down the motor:")
    car.cool_down()
    print_gas_status(car, "cooling down")
    
    # Test edge cases
    print("\n" + "="*40)
    print("EDGE CASES TEST")
    print("="*40)
    
    print("\n16. Trying to cool down when not overheated:")
    car.cool_down()
    print_gas_status(car, "cooling down when not overheated")
    
    print("\n17. Final operations - turn on and accelerate once more:")
    car.turn_on()
    print_gas_status(car, "final turn on")
    car.accelerate()
    print_gas_status(car, "final acceleration")
    
    # Summary
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    print(f"Total gas consumption: {car.get_gas_consumption()}")
    
    # Calculate expected consumption
    expected = (
        30 +    # Initial turn on
        10 +    # First acceleration
        30 +    # 3 multiple accelerations (3 × 10)
        30 +    # Second turn on (for overheating test)
        50 +    # 5 accelerations (5 × 10)
        50 +    # Overheating penalty
        20 +    # First overheated acceleration
        20 +    # Second overheated acceleration
        30 +    # Final turn on
        10      # Final acceleration
    )
    print(f"Expected gas consumption: {expected}")
    print(f"Match: {'✓' if car.get_gas_consumption() == expected else '✗'}")
    print("\n" + "="*60)
    print("GAS CONSUMPTION BREAKDOWN:")
    print("- Turn on from off: 30 gas each time")
    print("- Accelerate while on: 10 gas each time")
    print("- Overheating: 50 gas additional penalty")
    print("- Accelerate while overheated: 20 gas each time")
    print("- Brake/Turn off: 0 gas consumption")
    print("="*60)

if __name__ == "__main__":
    main()
