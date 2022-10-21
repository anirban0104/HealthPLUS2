#exec(open("1load.py").read())
#exec(open("2register.py").read())

#importing the required modules
from tkinter import *       # do pip install 
from tkinter import messagebox
from playsound import playsound

#playsound('sounds\\xpStart.mp3')
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.minsize(500,500)
root.title("HealthPLUS™ By Anirban & Dipanjana")

photo = PhotoImage(file = 'images/1.png')

root.iconphoto(False, photo)

mainLabel=Label(text="Welcome to HealthPLUS App, what is your issue?")
mainLabel.pack()
mainLabel2=Label(fg='red',text="Warning: No HealthApp can cure your issue better than a physical Doctor!")
mainLabel2.pack()

def allergies():
    print('''
Symptoms:
Symptoms
Sneezing.
Itching of the nose, eyes or roof of the mouth.
Runny, stuffy nose.
Watery, red or swollen eyes (conjunctivitis)


Treatment
The easiest and most effective way to treat allergies is to get rid of or avoid the cause. Where unavoidable, some lifestyle changes can reduce your allergy symptoms. For example, if you are allergic to dust mites, make an effort to keep your room clean and free of dust by frequent vacuuming, dusting, and washing of bedding.

For pollen allergies, avoid being outside when pollen counts are high and keep the windows to your room shut.

Because it is very difficult to avoid certain allergens, medication may be necessary to lessen symptoms caused by allergens, other than food and drugs.

Antihistamines: help relieve or prevent the sneezing, itchy eyes and throat, and postnasal drip that the allergen may cause. They are sold in many forms (i.e., pills, nasal sprays, liquids, etc.).
Decongestants: help reduce congestion in your nasal membranes by narrowing the blood vessels that supply those membranes. They can be purchased in several forms (liquid, pill or nasal spray) and may be used with an antihistamine or alone to treat nasal swelling related to allergies.  Limit use of nasal sprays to fewer than two to three days in a row because prolonged use can cause the nasal membrane swells, resulting in severe nasal obstruction. 
Anti-inflammatory agents (e.g., corticosteroid): help reduce swelling of the airways, nasal congestion and sneezing. Typically taken as a nasal spray. Some people report that corticosteroids irritate nasal passages.
Allergy shots: recommended for serious allergy sufferers, this series of shots are administered by a healthcare provider and contain small amounts of the allergens that cause you discomfort. The goal of allergy shots is to enable your immune system to build better defenses against allergens.
Some allergies go away with age, but others are lifelong.
    ''')

def cold_and_flu():
    print('''

    Symptoms: 

    The symptoms of flu can include fever or feeling feverish/chills, cough, sore throat, runny or stuffy nose, muscle or body aches, headaches, and fatigue (tiredness). Cold symptoms are usually milder than the symptoms of flu. People with colds are more likely to have a runny or stuffy nose.
    Rest more than usual and avoid exercise until symptoms are gone.

    Remedy: 
Drink lots of clear fluids (e.g., water, tea).
Stay away from cigarette smoke.
Do not take antibiotics unless specifically prescribed for you to cure the illness from which you currently suffer.
Avoid drinking alcohol because it weakens your immune system and may interact with medications.
Avoid caffeine, which can increase congestion and dehydration.
Eat a well-balanced diet, including fruits, vegetables, and grains.
    ''')

def conjunctivitis():
    print('''

    Symptoms
Pink or red color in the white of the eye(s)
Swelling of the conjunctiva (the thin layer that lines the white part of the eye and the inside of the eyelid) and/or eyelids.
Increased tear production.
Feeling like a foreign body is in the eye(s) or an urge to rub the eye(s)
Itching, irritation, and/or burning.

Cure: 
    Wash your hands frequently to prevent spreading an existing infection to your other eye, and to other people.
Don’t rub your eyes.
Use a cool wet washcloth to soak off any crusting.
Use a warm or cool compress to reduce discomfort.
Discard eye make-up because it may cause future infection.
Wash any clothing that may be contaminated, including towels and pillowcases. Try to use clean towels and pillowcases everyday.
Avoid wearing contact lenses and discard current lenses.
If eye drops are prescribed, place drop in pocket formed by pulling down lower lid. Make sure you don’t touch the bottle to the eye in order to prevent contamination.
If the infection does not improve in 2 or 3 days, make an appointment for re-evaluation.
''')

def diarrhea():
    print('''

    Symptoms: 
    Abdominal cramps or pain.
Bloating.
Nausea.
Vomiting.
Fever.
Blood in the stool.
Mucus in the stool.
Urgent need to have a bowel movement.


Avoid foods that are milk-based, greasy, high-fiber, or very sweet because these are likely to aggravate diarrhea.
Avoid caffeine and alcohol.
Do not eat solid food if you have signs of dehydration (thirst, light-headed, dark urine). Instead, drink about 2 cups of clear fluids per hour (if vomiting isn’t present), such as sports drinks and broth. Water alone is not enough because your body needs sodium and sugar to replace what it’s losing.
Avoid high sugar drinks, like apple juice, grape juice, and soda, which can pull water into the intestine and make the diarrhea persist.
Don’t drink clear liquids exclusively for more than 24 hours.
Begin eating normal meals within 12 hours, but stick to food that is bland and won’t irritate your intestine. Some doctors suggest the “BRAT“ diet which includes foods that are low in fiber, fat, and sugar. BRAT stands for Bananas, Rice, Applesauce, and Toast.
Use over-the-counter lactobacillus acidophilus capsules or tablets. These bacteria help maintain a healthy intestine, and are found in yogurt with live active cultures.
Decrease level of exercise until symptoms are gone.
Over-the-counter drugs, such as Imodium A-D, should only be used if absolutely necessary because it is important to let diarrhea flush out the bacteria or parasite that’s causing the infection.
''')

def headaches():
    print("""

Symptoms: 

Fever.
Infection.
High blood pressure.
Muscle weakness, numbness or tingling.
Excessive fatigue.
Loss of consciousness.
Balance problems and frequent falls.

Cure: 

Ice pack held over the eyes or forehead
Heating pad set on low or hot shower to relax tense neck and shoulder muscles
Sleep, or at least resting in a dark room
Taking breaks from stressful situations
Regular exercise to increase endorphin levels and relax muscles. Even if you already have a headache, exercising may relieve the pain. However, intense exercise may bring on a headache.
Occasional use of over-the-counter medicines such as acetaminophen, ibuprofen, or aspirin can relieve both migraine and tension headaches. *
Prescription drugs for severe headaches
    """)

def mononucleosis():
    print('''
    Signs and symptoms of mononucleosis may include:
Fatigue.
Sore throat, perhaps misdiagnosed as strep throat, that doesn't get better after treatment with antibiotics.
Fever.
Swollen lymph nodes in your neck and armpits.
Swollen tonsils.
Headache.
Skin rash.
Soft, swollen spleen.

Cure: 
        Mono is a virus, so antibiotics won’t help. Make sure you get plenty of rest, eat healthy foods, avoid alcohol (because your liver may be inflamed and drinking weakens immune responses), drink plenty of fluids, take aspirin or an aspirin substitute to reduce pain and fever, gargle salt water to relieve sore throat, and avoid strenuous activity. Because your spleen may be swollen, it is important not to engage in contact sports which could rupture your spleen. Returning to normal activity too quickly increases your chances of relapse.
''')
def stomach_aches():
    stomach_aches_choice= input("Press 1 to view remdedy for INTESTINAL GAS or leave blank to view remedy for NAUSEA AND VOMITING: ")
    if stomach_aches_choice=="1":
        print('''
        To prevent gas:

Avoid foods that trigger gas.
Avoid swallowing excess air by not chewing gum or eating hard candy.
Take digestive enzyme supplements, such as Beano (for high-fiber foods) and lactase supplements (for milk products).
Eat only small amounts of dairy products with food, if you suspect lactose intolerance.
Eat several small meals throughout the day instead of two or three larger ones.
Eat slowly, in a relaxed setting, and chew your food thoroughly.
Take a stroll after meals. Don’t sit in a slumped position or lie down after eating.
If increasing the fiber in your diet, do so gradually
Exercise to facilitate the passage of gas through the digestive tract.
        ''')
    else:
        vomit_choice=input("Press 1 to view remedy for Self-care tips for vomiting or leave blank to see remedy for nausea without vomiting: ")
        if vomit_choice=="1":
            print('''
            Wait 30-60 minutes after vomiting before drinking anything to let your stomach settle.
Don’t eat solid foods. Don’t drink milk.
Drink clear liquids, taking small sips. Stir any carbonated beverages to get all the bubbles out before sipping them. Suck on ice chips if nothing else will stay down.
Gradually return to regular diet, but wait about 8 hours from the last time you vomited. Start with foods like dry toast, crackers, rice, and other foods that are easy to digest.
Avoid substances that irritate the stomach, like alcohol, aspirin, and fried foods.
Avoid diuretics, like caffeine and alcohol, that contribute to fluid loss.
            ''')
        else:
            print('''
            Drink clear liquids. Eat small amounts of dry foods, such as soda crackers, if tolerated.
Avoid things that irritate the stomach, such as alcohol, aspirin, spicy, and fried foods.
For motion sickness, use an over-the-counter anti-nausea medicine, such as Dramamine.
            ''')

frame = Frame(root, borderwidth=10, bg="white", relief=SUNKEN)
frame.pack(side=BOTTOM, anchor="nw")


#creating the buttons
b1 = Button(frame, fg="black", text="Allergies", command=allergies)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="black", text="Colds and Flu", command=cold_and_flu)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="black", text="Conjunctivitis (Pink Eye)", command=conjunctivitis)
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="black", text="Diarrhea", command=diarrhea)
b4.pack(side=LEFT, padx=23)

b5 = Button(frame, fg="black", text="Headaches", command=headaches)
b5.pack(side=LEFT, padx=23)

b6 = Button(frame, fg="black", text="Mononucleosis", command=mononucleosis)
b6.pack(side=LEFT, padx=23)

b7 = Button(frame, fg="black", text="Stomach Aches", command=stomach_aches)
b7.pack(side=LEFT, padx=23)

b8 = Button(frame, fg="red", text="Quit", command=root.destroy)
b8.pack(side=LEFT, padx=23)

root.mainloop()