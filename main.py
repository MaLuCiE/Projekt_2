"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Lucie Mazánková
email: lucie.mazankova@centrum.cz
"""
import random
import time

separator = "-" * 47

def measure_time(start):
    """
    Funkce pro výpočet uplynulého času od start začátku hry.
    Vrací float uplynulý čas v sekundách.
    """
    return time.time() - start

def say_hello():
    """Tisk úvodní zprávy pro hráče"""
    print("Hi there!")
    print(separator)
    print("I've generated a random 4-digit number for you.")
    print("Let's play a bulls and cows game.")
    print(separator)
    print("You can exit the game by pressing 'Q'.")
    print(separator)

def generate_secret_number():
    """
    Vygeneruje náhodné čtyřciferné číslo, které nezačíná nulou a neobsahuje duplicity.
    Vrací string náhodné čtyřciferné číslo jako řetězec.
    """
    number = random.sample("1234567890", 4)
    while number[0] == "0":
        number = random.sample("1234567890", 4)
    return "".join(number)

def check_tip(tip):
    """
    Ověří zda je vstupní číslo hráče platné.
    Vrací string nebo None: Chybová zpráva, pokud je vstup neplatný, jinak None.
    """
    # Kontrole délky a jiných znaků než čísla
    if not tip.isdigit() or len(tip) != 4:
        return "The number must consist of exactly 4 digits and include digits only."  
    
    # Ověření, že číslo nezačíná nulou
    if tip[0] == '0':
        return "The number should not start with the digit 0."
    
    # Kontrola duplicitních čísel
    if len(set(tip)) != len(tip):
        return "Each digit in the number must be unique."
    
    return None

def compare_tip(secret_number, tip):
    """
    Porovnání vygenerovného čísla a čísla, které uvedl hráč
    Vrací tuple počet bulls (správné číslice na správných pozicích) a cows (správné číslice na nesprávných pozicích).
    """
    bulls = 0
    cows = 0
    
    for a, b in zip(secret_number, tip):
        if a == b:
            bulls += 1
        elif b in secret_number:
            cows += 1
    return bulls, cows

def print_result(bulls, cows):
    """
    Vypíše výsledek vyhodnocení.
    """

    if bulls == 1:
        bull_text = "1 bull"
    else:
        bull_text = f"{bulls} bulls"
    
    if cows == 1:
        cow_text = "1 cow"
    else:
        cow_text = f"{cows} cows"
    
    print(f"{bull_text}, {cow_text}")

def main():
    """
    Spuštění hry Bulls and Cows.
    Tento kód se spustí jen při přímém spuštění.
    """
    say_hello()
    secret_number = generate_secret_number()
    attemps = 0
    start = time.time()

    while True:
        tip = input("Enter a number: ")
        
        # Ukončení hry
        if tip.upper() == 'Q':
            print("You chose to quit. The secret number was:", secret_number)
            print(separator)
            print(f"Time taken: {elapsed_time:.2f} seconds.")
            break
        
        # Ověření, zda je tip zadán dle pravidel
        fail = check_tip(tip)
        if fail:
            print(fail)
            continue

        attemps += 1
        bulls, cows = compare_tip(secret_number, tip)
        print_result(bulls, cows)

        print(separator) 

        # když hráč uhodne číslo
        if bulls == 4:
            elapsed_time = measure_time(start)
            print(f"Correct, you've guessed the right number in {attemps} attempts.")
            print(f"Time taken: {elapsed_time:.2f} seconds.")
            print(separator)
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()