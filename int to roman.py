class IntToRoman:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        num = self.number
        roman_num = ""
        for i in range(len(val)):
            count = num // val[i]
            roman_num += syms[i] * count
            num -= val[i] * count
        return roman_num

# Example usage:
num = int(input("Enter an integer: "))
converter = IntToRoman(num)
print(f"Roman numeral: {converter.to_roman()}")