class Calculator:
    def add(self, a, b):
        # การบวกยังคงถูกต้องอยู่
        return a + b

    def subtract(self, a, b):
        # การลบยังคงถูกต้องอยู่
        return a + (-b)

    def multiply(self, a, b):
        result = 0
        negative = False
        
        # ตรวจสอบเครื่องหมาย
        if a < 0 and b < 0:
            a, b = -a, -b
        elif b < 0:
            b = -b
            negative = True
        elif a < 0:
            a = -a
            negative = True

        # ใช้การบวกซ้ำแทนการคูณ
        for _ in range(b):
            result += a

        # ถ้าผลลัพธ์ควรเป็นค่าลบ
        if negative:
            result = -result
        
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = 0
        negative = False

        # ตรวจสอบเครื่องหมาย
        if a < 0 and b < 0:
            a, b = -a, -b
        elif b < 0:
            b = -b
            negative = True
        elif a < 0:
            a = -a
            negative = True

        # ใช้การลบซ้ำแทนการหาร
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        # ถ้าผลลัพธ์ควรเป็นค่าลบ
        if negative:
            result = -result
        
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot modulo by zero")
        
        negative = a < 0
        a = abs(a)
        b = abs(b)

        # ใช้การลบซ้ำหาค่าเศษเหลือ
        while a >= b:
            a = self.subtract(a, b)

        # คืนค่าผลลัพธ์ที่ถูกต้องในกรณีค่าลบ
        return -a if negative else a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: multiplication: ", calc.multiply(-2, 3))
    print("Example: multiplication: ", calc.multiply(2, -3))
    print("Example: multiplication: ", calc.multiply(-2, -3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))