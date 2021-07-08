class Operations:
    def __init__(self):
        self.value = 0
        self.temporary = 0

    def Add(self, A, B):
        result = ""
        carry = 0
        A = list(A[ : :-1])
        B = list(B[ : :-1])

        for i, j in zip(A, B):
            if i == "0" and j == "0":
                if carry == 0:
                    result += "0"
                else:
                    result += "1"
                    carry = 0
            elif (i == "0" and j == "1") or (i == "1" and j == "0"):
                if carry == 0:
                    result += "1"
                else:
                    result += "0"
                    carry = 1
            else:
                if carry == 0:
                    result += "0"
                    carry = 1
                else:
                    result += "1"
                    carry = 1

        return result[ : : -1]


    def BinaryValue(self, number):
        if number > 1:
            self.BinaryValue(number // 2)

        self.value += str(number % 2)

    def Binary(self, number):
        self.value = ""
        if number >= 0:
            self.BinaryValue(number)
            self.value = self.value.rjust(10, "0")
        else:
            self.BinaryValue(int(str(number)[1 : ]))
            self.value = self.value.rjust(10, "0")
            self.temporary = ""

            # Converting the binary value into its one's complement
            for i in self.value:
                if i == "0":
                    self.temporary += "1"
                else:
                    self.temporary += "0"

            self.temporary = list(self.temporary)

            # Adding 1 to the one's complement to get the two's complement
            for i in range(9, -1, -1):
                if self.temporary[i] == "1":
                    self.temporary[i] = "0"
                elif self.temporary[i] == "0":
                    self.temporary[i] = "1"
                    break

            self.value = "".join(self.temporary)

        return self.value

Object = Operations()
Bits = 10
A = "0" * Bits
Multiplicand = int(input("Enter the Multiplicand : "))    # Integer value of the multiplier (It will further store the binary value)
NegativeMultiplicand = ""                                 # For storing negative binary value of the multiplicand
First = Multiplicand                                      # Integer value of the multiplier
Second =  int(input("Enter the Multiplier : "))           # Integer value of the multiplier
Multiplier = Object.Binary(Second)                        # Binary value of the multiplier
sign = ""
if (First > 0 and Second > 0) or (First < 0 and Second < 0):
    sign = "+"
else:
    sign = "-"

Q = "0"                                                   # Stores the Q[-1] bit
Q0 = Multiplier[-1]                                       # Stores the Q[0] bit
count = Bits                                              # Maintain the step counter
Tasks = ("Right Shift", "(A = A - M) + Right Shift", "(A = A + M) + Right Shift", "Initialization")

# Printing the Table Header
print("\n-----" + "   " + "---------".center(25) + "   " + "----------" + "   " + "----------" + "   " + "-----" + "   " + "----------")
print("COUNT" + "   " + "OPERATION".center(25) + "   " + "REGISTER-A" + "   " + "MULTIPLIER" + "   " + "Q[-1]" + "   " + "Q[0] Q[-1]")
print("-----" + "   " + "---------".center(25) + "   " + "----------" + "   " + "----------" + "   " + "-----" + "   " + "----------")
print(str(count).rjust(5, "0") + "   " + Tasks[-1].center(25) + "   " + str(A) + "   " + Multiplier + "   " + Q.center(5) + "   " + str(Q0).center(5) + " " + str(Q).center(5))

# Finding the product
Multiplicand = Object.Binary(First)                   # M : Multiplicand
NegativeMultiplicand = Object.Binary(-First)          # -M : Negative of Multiplicand
String = A + Multiplier + Q                           # A string that includes the register A, multiplier and Q[-1] bit
task = 0                                              # To choose the operation for each count

while count != 0:
    if (Q0 + Q) == "00" or (Q0 + Q) == "11":
        # Right Shifting
        String = String[0] + String[ : -1]
        task = 0
        A = String[ : 10]
        Multiplier = String[10 : 20]
        Q0 = Multiplier[-1]
        Q = String[-1]
    else:
        if (Q0 + Q) == "10":
            task = 1
            # A = A - M
            A = Object.Add(A, NegativeMultiplicand)
            # Right Shifting
            String = A + Multiplier + Q
            String = String[0] + String[ : -1]
            A = String[ : 10]
            Multiplier = String[10 : 20]
            Q0 = Multiplier[-1]
            Q = String[-1]
        else:
            task = 2
            # A = A + M
            A = Object.Add(A, Multiplicand)
            # Right Shifting
            String = A + Multiplier + Q
            String = String[0] + String[ : -1]
            A = String[ : 10]
            Multiplier = String[10 : 20]
            Q0 = Multiplier[-1]
            Q = String[-1]

    count -= 1
    print(str(count).rjust(5, "0") + "   " + Tasks[task].center(25) + "   " + str(A) + "   " + Multiplier + "   " + Q.center(5) + "   " + str(Q0).center(5) + " " + str(Q).center(5))

# Printing the results
print("\n-------\nRESULTS\n-------\n")
BinaryResult = A + Multiplier
x = ""
PreviousResultOne = "0"

if BinaryResult[0] == "1":
    PreviousResultOne = BinaryResult

    for i in BinaryResult:
        if i == "0":
            x += "1"
        else:
            x += "0"

    BinaryResult = list(x)
    PreviousResultTwo = x

    for i in range((2 * Bits) - 1, -1, -1):
        if BinaryResult[i] == "1":
            BinaryResult[i] = "0"
        elif BinaryResult[i] == "0":
            BinaryResult[i] = "1"
            break

    BinaryResult = "".join(BinaryResult)

IntegerResult = 0

for i in range(1, (2 * Bits) + 1):
    if BinaryResult[2 * Bits - i] == "1":
        IntegerResult += 2 ** (i - 1)

if IntegerResult == 0:
    print("Integer Value : " + str(IntegerResult))
else:
    print("Integer Value : " + sign + str(IntegerResult))
if PreviousResultOne[0] == "1":
    print("Binary Value : " + PreviousResultOne + " --> " + PreviousResultTwo + " + 1 --> " +BinaryResult)
else:
    print("Binary Value : " + BinaryResult)
