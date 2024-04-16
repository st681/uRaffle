from readTasks import readTasks
from processors import processorMapping
from termcolor import colored

def chooseProcessor():
    print(colored('Available Raffle Processors:', 'magenta'))
    for idx, name in enumerate(processorMapping, start=1):
        print(colored(f"{idx}. {name}",'magenta'))

    choice = input('Enter the number of the raffle processor to use: ')
    try:
        selected_name = list(processorMapping.keys())[int(choice) - 1]
        processor_class = processorMapping[selected_name]
        return processor_class()
    except (IndexError, ValueError):
        print(colored('Invalid selection. Please try again.', 'red'))
        return chooseProcessor()
    
def main():
    print('''
██████╗░░█████╗░███████╗███████╗██╗░░░░░███████╗  ░█████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝███████║█████╗░░█████╗░░██║░░░░░█████╗░░  ██║░░╚═╝██║░░██║██║░░██║█████═╝░█████╗░░██████╔╝
██╔══██╗██╔══██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░  ██║░░██╗██║░░██║██║░░██║██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║██║░░░░░██║░░░░░███████╗███████╗  ╚█████╔╝╚█████╔╝╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝  ░╚════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
        ''')
    print(colored('made by stupit\n', 'blue'))
    processor = chooseProcessor()
    bot = readTasks('tasks.csv', processor)
    bot.processEntries()

if __name__ == "__main__":
    main()
