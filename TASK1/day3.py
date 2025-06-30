def sum_even_numbers(numbers):
    """Returns the sum of all even numbers in the list."""
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

if __name__ == "__main__":
    
    sample_list = [1, 2, 3, 4, 5, 6, 5, 7, 11, 8, 10, 12, 14, 16]
    print("List:", sample_list)
    print("Sum of even numbers:", sum_even_numbers(sample_list))
    