from entryProcessor import EntryProcessor
from utils.infoGens import generateBirthday
from utils.inputValidators import validateEmail, validateProxy
import asyncio
import nodriver as uc
import random
from termcolor import colored
import time


class arcadeFire(EntryProcessor):
    def requiredFields(self):
        return ["email", "proxy"]
    
    async def process(self, entry):
        if not validateEmail(entry['email']):
            print(colored("Invalid email, skipping task",'red'))
            return

        proxyDetails = None
        if entry['proxy']:
            try:
                proxyDetails = validateProxy(entry['proxy'])
            except ValueError as ve:
                print(ve)
                return

    
        print(colored(f"Processing entry for {entry['email']}",'green')) 
        birthday = generateBirthday()

        try:
            if proxyDetails:
                #add code to load proxy
                browser = await uc.start()
            else:
                browser = await uc.start()

            page = await browser.get('https://forms.sonymusicfans.com/campaign/columbia_arcadefire_2022/')

        except Exception as e:
            print(colored(f"An error occurred: {str(e)}", 'red'))
        
        finally:
                if 'browser' in locals():
                    browser.stop()