"""
Extended sample data generator with 10 clinical conversation cases.
Covers diverse scenarios similar to the paper's 16 simulated visits.

Scenarios:
  case_01: Persistent cough + shortness of breath
  case_02: Chronic headaches
  case_03: Lower back pain
  case_04: Diabetes management / blood sugar control
  case_05: Chest pain / cardiac concerns
  case_06: Abdominal pain + digestive issues
  case_07: Anxiety and sleep problems
  case_08: Knee pain / joint issues
  case_09: Skin rash / allergic reaction
  case_10: Fatigue and weight gain / thyroid concerns
"""

import json
from pathlib import Path


SAMPLE_CASES = [
    {
        "id": "case_01",
        "lines": [
            {"speaker": "Provider", "text": "So what brings you in here today?"},
            {"speaker": "Patient", "text": "I've been having this persistent cough for about three weeks now, and I'm also getting shortness of breath."},
            {"speaker": "Provider", "text": "I see. When did the cough first start?"},
            {"speaker": "Patient", "text": "It started about three weeks ago, maybe a little more. It's been getting worse lately."},
            {"speaker": "Provider", "text": "Is it a dry cough or are you producing any mucus?"},
            {"speaker": "Patient", "text": "It's mostly dry, but sometimes I notice a little bit of yellowish mucus."},
            {"speaker": "Provider", "text": "Have you had any fever or chills?"},
            {"speaker": "Patient", "text": "I've had some low-grade fevers, maybe around 99 to 100 degrees."},
            {"speaker": "Provider", "text": "Any chest pain with the coughing?"},
            {"speaker": "Patient", "text": "A little bit, yeah. It hurts when I take a deep breath sometimes."},
            {"speaker": "Provider", "text": "Are you a smoker or have you been around anyone who is sick?"},
            {"speaker": "Patient", "text": "I quit smoking about two years ago. I smoked for about 15 years before that. And my coworker was sick last month with something similar."},
            {"speaker": "Provider", "text": "Do you have any allergies or are you taking any medications currently?"},
            {"speaker": "Patient", "text": "I take lisinopril for my blood pressure, and I have a seasonal allergy to pollen."},
            {"speaker": "Provider", "text": "How is your blood pressure been? Have you been checking it at home?"},
            {"speaker": "Patient", "text": "It's been okay, usually around 130 over 85. I check it once a week."},
            {"speaker": "Provider", "text": "Have you noticed any wheezing or difficulty breathing at night?"},
            {"speaker": "Patient", "text": "Actually yes, I've been waking up at night a couple of times because I feel like I can't breathe well."},
            {"speaker": "Provider", "text": "How about your appetite and weight? Any changes recently?"},
            {"speaker": "Patient", "text": "My appetite has been down a bit, but I haven't really noticed any weight loss."},
            {"speaker": "Provider", "text": "Any recent travel or exposure to chemicals or dust at work?"},
            {"speaker": "Patient", "text": "No travel, but I work in a warehouse and there's a lot of dust there."},
            {"speaker": "Provider", "text": "Alright. Let me listen to your lungs and we'll go from there."},
            {"speaker": "Patient", "text": "Sounds good. I'm just worried it might be something serious since it's been going on so long."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient is experiencing persistent cough with shortness of breath for three weeks."},
            {"line_idx": 3, "type": "detail", "summary": "Cough started approximately three weeks ago and has been worsening."},
            {"line_idx": 5, "type": "detail", "summary": "Cough is mostly dry with occasional yellowish mucus production."},
            {"line_idx": 7, "type": "detail", "summary": "Patient has been experiencing low-grade fevers around 99-100 degrees."},
            {"line_idx": 9, "type": "detail", "summary": "Patient reports chest pain with deep breathing during coughing."},
            {"line_idx": 11, "type": "detail", "summary": "Patient is a former smoker who quit two years ago after 15 years. Coworker was recently sick with similar symptoms."},
            {"line_idx": 13, "type": "detail", "summary": "Patient takes lisinopril for blood pressure and has seasonal pollen allergy."},
            {"line_idx": 15, "type": "detail", "summary": "Blood pressure readings around 130/85, checked weekly at home."},
            {"line_idx": 17, "type": "detail", "summary": "Patient experiences nocturnal dyspnea, waking up at night with difficulty breathing."},
            {"line_idx": 19, "type": "detail", "summary": "Decreased appetite but no noticeable weight loss."},
            {"line_idx": 21, "type": "detail", "summary": "No recent travel but occupational dust exposure in warehouse work environment."},
        ],
    },
    {
        "id": "case_02",
        "lines": [
            {"speaker": "Provider", "text": "Good morning. How can I help you today?"},
            {"speaker": "Patient", "text": "Hi, I've been having really bad headaches for the past two weeks. They come almost every day now."},
            {"speaker": "Provider", "text": "I'm sorry to hear that. Can you describe the headaches? Where do you feel the pain?"},
            {"speaker": "Patient", "text": "It's usually on both sides of my head, kind of like a tight band around my forehead. Sometimes it goes to the back of my neck too."},
            {"speaker": "Provider", "text": "How would you rate the pain on a scale from 1 to 10?"},
            {"speaker": "Patient", "text": "It's usually about a 6 or 7. Sometimes it gets up to an 8 when it's really bad."},
            {"speaker": "Provider", "text": "Do you notice anything that triggers the headaches?"},
            {"speaker": "Patient", "text": "Stress seems to make them worse. I've been under a lot of pressure at work lately. Also, I've been spending a lot of time on the computer."},
            {"speaker": "Provider", "text": "Any nausea, vomiting, or sensitivity to light?"},
            {"speaker": "Patient", "text": "No nausea or vomiting, but I do get a bit sensitive to bright lights when the headache is bad."},
            {"speaker": "Provider", "text": "Have you tried any over-the-counter medications?"},
            {"speaker": "Patient", "text": "I've been taking ibuprofen, about 400mg, two or three times a day. It helps a little but doesn't fully go away."},
            {"speaker": "Provider", "text": "How's your sleep been? Are you getting enough rest?"},
            {"speaker": "Patient", "text": "Honestly, not great. I've been sleeping maybe 5 hours a night. I have trouble falling asleep because of the stress."},
            {"speaker": "Provider", "text": "Do you drink caffeine regularly?"},
            {"speaker": "Patient", "text": "Yeah, I probably have about 4 or 5 cups of coffee a day. Sometimes more when I'm really tired."},
            {"speaker": "Provider", "text": "Any changes in your vision or any numbness or tingling?"},
            {"speaker": "Patient", "text": "No, nothing like that."},
            {"speaker": "Provider", "text": "Any history of headaches or migraines in your family?"},
            {"speaker": "Patient", "text": "My mom gets migraines. She's been dealing with them her whole life."},
            {"speaker": "Provider", "text": "Okay, let me do a quick neurological exam and we'll talk about a plan."},
            {"speaker": "Patient", "text": "That would be great. I just want to find something that works because it's really affecting my work."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient is experiencing daily severe headaches for the past two weeks."},
            {"line_idx": 3, "type": "detail", "summary": "Headaches are bilateral with tight band sensation around forehead, sometimes extending to back of neck."},
            {"line_idx": 5, "type": "detail", "summary": "Pain severity is usually 6-7 out of 10, sometimes reaching 8."},
            {"line_idx": 7, "type": "detail", "summary": "Headaches triggered by stress and prolonged computer use at work."},
            {"line_idx": 9, "type": "detail", "summary": "No nausea or vomiting but photosensitivity present during severe episodes."},
            {"line_idx": 11, "type": "detail", "summary": "Patient taking ibuprofen 400mg two to three times daily with partial relief."},
            {"line_idx": 13, "type": "detail", "summary": "Patient sleeping only about 5 hours per night due to stress-related insomnia."},
            {"line_idx": 15, "type": "detail", "summary": "High caffeine intake of 4-5 cups of coffee daily."},
            {"line_idx": 17, "type": "detail", "summary": "No vision changes, numbness, or tingling reported."},
            {"line_idx": 19, "type": "detail", "summary": "Family history of migraines in mother."},
        ],
    },
    {
        "id": "case_03",
        "lines": [
            {"speaker": "Provider", "text": "What brings you in today?"},
            {"speaker": "Patient", "text": "I've been having some really bad lower back pain for about two months now. It's getting to the point where it's hard to do my daily activities."},
            {"speaker": "Provider", "text": "Can you point to where exactly the pain is?"},
            {"speaker": "Patient", "text": "It's right here in the lower back, kind of across the whole area. Sometimes it shoots down my left leg."},
            {"speaker": "Provider", "text": "Does the pain go all the way down to your foot or does it stop at the knee?"},
            {"speaker": "Patient", "text": "It usually stops around my knee, but once or twice it went all the way down to my ankle."},
            {"speaker": "Provider", "text": "Did anything specific trigger the pain?"},
            {"speaker": "Patient", "text": "I was helping my friend move about two months ago and I felt something pull in my back."},
            {"speaker": "Provider", "text": "On a scale of 1 to 10, how bad is the pain?"},
            {"speaker": "Patient", "text": "On a regular day it's about a 5 or 6, but when I bend over or sit for too long it goes up to an 8."},
            {"speaker": "Provider", "text": "Have you noticed any numbness or weakness in your legs?"},
            {"speaker": "Patient", "text": "Yeah, my left foot sometimes feels tingly, like pins and needles."},
            {"speaker": "Provider", "text": "Any changes in your bladder or bowel function?"},
            {"speaker": "Patient", "text": "No, that's all been normal."},
            {"speaker": "Provider", "text": "What have you been doing to manage the pain?"},
            {"speaker": "Patient", "text": "Tylenol and a heating pad. I also tried some stretches but they didn't help much."},
            {"speaker": "Provider", "text": "What kind of work do you do?"},
            {"speaker": "Patient", "text": "I work in an office, sitting at a desk for about 8 to 10 hours a day."},
            {"speaker": "Provider", "text": "Let me examine your back and test your reflexes."},
            {"speaker": "Patient", "text": "It's starting to affect my sleep too."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient presents with severe lower back pain for two months affecting daily activities."},
            {"line_idx": 3, "type": "detail", "summary": "Pain across entire lower back with radiation down the left leg."},
            {"line_idx": 5, "type": "detail", "summary": "Radiating pain usually stops at knee but occasionally extends to ankle."},
            {"line_idx": 7, "type": "detail", "summary": "Pain started two months ago after helping a friend move."},
            {"line_idx": 9, "type": "detail", "summary": "Baseline pain 5-6 out of 10, increases to 8 with bending or prolonged sitting."},
            {"line_idx": 11, "type": "detail", "summary": "Tingling and pins-and-needles sensation in left foot."},
            {"line_idx": 13, "type": "detail", "summary": "No bladder or bowel dysfunction."},
            {"line_idx": 15, "type": "detail", "summary": "Managing with Tylenol, heating pad, and stretches with limited relief."},
            {"line_idx": 17, "type": "detail", "summary": "Sedentary office work with 8-10 hours daily sitting."},
            {"line_idx": 19, "type": "detail", "summary": "Back pain also affecting sleep quality."},
        ],
    },
    {
        "id": "case_04",
        "lines": [
            {"speaker": "Provider", "text": "How have things been going with your diabetes management?"},
            {"speaker": "Patient", "text": "Not great. My blood sugars have been all over the place and I'm feeling really tired all the time."},
            {"speaker": "Provider", "text": "What have your blood sugar readings been like?"},
            {"speaker": "Patient", "text": "In the mornings they're around 180 to 200. After meals they sometimes go up to 250 or 300."},
            {"speaker": "Provider", "text": "Are you taking your medications as prescribed?"},
            {"speaker": "Patient", "text": "I take metformin twice a day but I miss the evening dose two or three times a week."},
            {"speaker": "Provider", "text": "What about your diet?"},
            {"speaker": "Patient", "text": "I've been eating out a lot because of work. I know I'm eating too many carbs."},
            {"speaker": "Provider", "text": "How about exercise?"},
            {"speaker": "Patient", "text": "I try to walk for about 20 minutes a few times a week but I just don't have the energy."},
            {"speaker": "Provider", "text": "Any changes in your vision?"},
            {"speaker": "Patient", "text": "My vision has been blurry in the mornings. It usually clears up after a couple of hours."},
            {"speaker": "Provider", "text": "Any numbness or tingling in your hands or feet?"},
            {"speaker": "Patient", "text": "My feet have been feeling numb at night for a few weeks now."},
            {"speaker": "Provider", "text": "When was your last eye exam?"},
            {"speaker": "Patient", "text": "Over a year ago."},
            {"speaker": "Provider", "text": "Let me check your A1C today and we'll review your treatment plan."},
            {"speaker": "Patient", "text": "I want to get this under control. I'm worried about the long-term effects."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient reports poor diabetes management with unstable blood sugars and persistent fatigue."},
            {"line_idx": 3, "type": "detail", "summary": "Fasting glucose 180-200, post-meal readings reaching 250-300."},
            {"line_idx": 5, "type": "detail", "summary": "On metformin twice daily but missing evening dose 2-3 times per week."},
            {"line_idx": 7, "type": "detail", "summary": "Frequent eating out with excessive carbohydrate intake."},
            {"line_idx": 9, "type": "detail", "summary": "Minimal exercise, walking 20 minutes a few times per week."},
            {"line_idx": 11, "type": "detail", "summary": "Morning blurry vision that resolves after a couple of hours."},
            {"line_idx": 13, "type": "detail", "summary": "Numbness in feet at night for past few weeks."},
            {"line_idx": 15, "type": "detail", "summary": "Last eye exam over a year ago."},
        ],
    },
    {
        "id": "case_05",
        "lines": [
            {"speaker": "Provider", "text": "I understand you've been having chest pain. Tell me about that."},
            {"speaker": "Patient", "text": "I've been getting pressure in my chest when I climb stairs or walk fast. It's been happening for about a week."},
            {"speaker": "Provider", "text": "Is it sharp, dull, or more like pressure?"},
            {"speaker": "Patient", "text": "It's like a heaviness right in the center of my chest. Like someone is sitting on it."},
            {"speaker": "Provider", "text": "Does the pain radiate anywhere?"},
            {"speaker": "Patient", "text": "A couple of times I felt it going into my left arm."},
            {"speaker": "Provider", "text": "How long does each episode last?"},
            {"speaker": "Patient", "text": "Usually about 5 to 10 minutes. It goes away when I stop and rest."},
            {"speaker": "Provider", "text": "Any shortness of breath, sweating, or nausea?"},
            {"speaker": "Patient", "text": "I get short of breath and sweaty when it happens. No nausea."},
            {"speaker": "Provider", "text": "Any history of heart disease or high cholesterol?"},
            {"speaker": "Patient", "text": "My cholesterol was around 240 last time. And my father had a heart attack at 55."},
            {"speaker": "Provider", "text": "Are you taking any medications for cholesterol?"},
            {"speaker": "Patient", "text": "I stopped atorvastatin about six months ago because of muscle cramps."},
            {"speaker": "Provider", "text": "Do you smoke or drink?"},
            {"speaker": "Patient", "text": "I don't smoke but I have a couple of beers most nights."},
            {"speaker": "Provider", "text": "How old are you?"},
            {"speaker": "Patient", "text": "I'm 52."},
            {"speaker": "Provider", "text": "I want to run an EKG right now and order some blood work."},
            {"speaker": "Patient", "text": "Whatever you think is best, doc."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient presents with exertional chest pressure for one week."},
            {"line_idx": 3, "type": "detail", "summary": "Chest sensation described as heaviness in center of chest."},
            {"line_idx": 5, "type": "detail", "summary": "Pain occasionally radiates to left arm."},
            {"line_idx": 7, "type": "detail", "summary": "Episodes last 5-10 minutes and resolve with rest."},
            {"line_idx": 9, "type": "detail", "summary": "Associated shortness of breath and sweating, no nausea."},
            {"line_idx": 11, "type": "detail", "summary": "Cholesterol around 240. Father had heart attack at age 55."},
            {"line_idx": 13, "type": "detail", "summary": "Discontinued atorvastatin six months ago due to muscle cramps."},
            {"line_idx": 15, "type": "detail", "summary": "Non-smoker, drinks a couple of beers most nights."},
            {"line_idx": 17, "type": "detail", "summary": "Patient is 52 years old."},
        ],
    },
    {
        "id": "case_06",
        "lines": [
            {"speaker": "Provider", "text": "Hi there. What brings you in today?"},
            {"speaker": "Patient", "text": "I've been having stomach pain and bloating for about three weeks. It's getting worse."},
            {"speaker": "Provider", "text": "Where exactly is the pain?"},
            {"speaker": "Patient", "text": "Upper part of my stomach, sometimes it moves to the right side."},
            {"speaker": "Provider", "text": "Is the pain constant or does it come and go?"},
            {"speaker": "Patient", "text": "It comes and goes. Worst after big meals or fatty foods."},
            {"speaker": "Provider", "text": "Any nausea, vomiting, or diarrhea?"},
            {"speaker": "Patient", "text": "Some nausea after meals. No vomiting but loose stools three or four times a week."},
            {"speaker": "Provider", "text": "Any blood in your stool?"},
            {"speaker": "Patient", "text": "No, nothing like that."},
            {"speaker": "Provider", "text": "Any heartburn or acid reflux?"},
            {"speaker": "Patient", "text": "Yes, burning sensation in my chest after eating, especially when I lie down."},
            {"speaker": "Provider", "text": "What's your diet like?"},
            {"speaker": "Patient", "text": "A lot of fast food and spicy food. Coffee in the morning and soda all day."},
            {"speaker": "Provider", "text": "Any medications?"},
            {"speaker": "Patient", "text": "Daily aspirin for my heart, and Tums almost every day for the past two weeks."},
            {"speaker": "Provider", "text": "Any weight loss?"},
            {"speaker": "Patient", "text": "About 5 pounds in the last month without trying."},
            {"speaker": "Provider", "text": "Let me do an abdominal exam."},
            {"speaker": "Patient", "text": "I hope it's nothing serious."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient presents with worsening stomach pain and bloating for three weeks."},
            {"line_idx": 3, "type": "detail", "summary": "Pain in upper abdomen, sometimes migrating to right side."},
            {"line_idx": 5, "type": "detail", "summary": "Intermittent pain worsened by large or fatty meals."},
            {"line_idx": 7, "type": "detail", "summary": "Post-meal nausea, loose stools 3-4 times per week."},
            {"line_idx": 9, "type": "detail", "summary": "No blood in stool."},
            {"line_idx": 11, "type": "detail", "summary": "Heartburn and burning chest sensation after eating, worse when lying down."},
            {"line_idx": 13, "type": "detail", "summary": "Diet high in fast food, spicy food, coffee, and soda."},
            {"line_idx": 15, "type": "detail", "summary": "Takes daily aspirin and Tums almost daily for two weeks."},
            {"line_idx": 17, "type": "detail", "summary": "Unintentional weight loss of 5 pounds in one month."},
        ],
    },
    {
        "id": "case_07",
        "lines": [
            {"speaker": "Provider", "text": "How are you doing today?"},
            {"speaker": "Patient", "text": "I've been feeling really anxious for the past month. I can't relax no matter what I do."},
            {"speaker": "Provider", "text": "Can you tell me more about what the anxiety feels like?"},
            {"speaker": "Patient", "text": "My heart races, I get sweaty palms, and there's tightness in my chest. I feel like something terrible is about to happen."},
            {"speaker": "Provider", "text": "Have you had any panic attacks?"},
            {"speaker": "Patient", "text": "Two weeks ago at the grocery store my heart was pounding, I couldn't breathe, and I felt dizzy."},
            {"speaker": "Provider", "text": "How is this affecting your daily life?"},
            {"speaker": "Patient", "text": "I've been avoiding going out. I called in sick to work three times last week."},
            {"speaker": "Provider", "text": "How has your sleep been?"},
            {"speaker": "Patient", "text": "I lie in bed for hours worrying. When I fall asleep I wake up at 3 or 4 AM."},
            {"speaker": "Provider", "text": "Is there anything specific causing you stress?"},
            {"speaker": "Patient", "text": "My mom was diagnosed with cancer two months ago. I'm trying to help care for her while working full time."},
            {"speaker": "Provider", "text": "Any changes in eating habits?"},
            {"speaker": "Patient", "text": "I barely eat. I've lost about 8 pounds in the last month."},
            {"speaker": "Provider", "text": "Are you using any substances to cope?"},
            {"speaker": "Patient", "text": "More wine at night, maybe a bottle every couple of days. And lots of coffee."},
            {"speaker": "Provider", "text": "Have you been treated for anxiety or depression before?"},
            {"speaker": "Patient", "text": "I was on Lexapro about five years ago for depression. Stopped after a year."},
            {"speaker": "Provider", "text": "Any thoughts of hurting yourself?"},
            {"speaker": "Patient", "text": "No, nothing like that. Just overwhelmed and exhausted."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient reports persistent anxiety and inability to relax for one month."},
            {"line_idx": 3, "type": "detail", "summary": "Symptoms include racing heart, sweaty palms, chest tightness, and sense of impending doom."},
            {"line_idx": 5, "type": "detail", "summary": "Panic attack at grocery store with palpitations, dyspnea, and dizziness."},
            {"line_idx": 7, "type": "detail", "summary": "Avoidance behavior, missed three days of work last week."},
            {"line_idx": 9, "type": "detail", "summary": "Severe insomnia with early morning awakening at 3-4 AM."},
            {"line_idx": 11, "type": "detail", "summary": "Mother diagnosed with cancer two months ago. Patient is caregiver while working full time."},
            {"line_idx": 13, "type": "detail", "summary": "Poor appetite with 8-pound weight loss in one month."},
            {"line_idx": 15, "type": "detail", "summary": "Increased alcohol and caffeine use to cope."},
            {"line_idx": 17, "type": "detail", "summary": "Previous depression treated with Lexapro five years ago."},
            {"line_idx": 19, "type": "detail", "summary": "Denies suicidal ideation."},
        ],
    },
    {
        "id": "case_08",
        "lines": [
            {"speaker": "Provider", "text": "What's going on today?"},
            {"speaker": "Patient", "text": "My right knee has been really bothering me for six weeks. I can barely walk up stairs."},
            {"speaker": "Provider", "text": "Did anything trigger the pain?"},
            {"speaker": "Patient", "text": "I play basketball on weekends and it just started hurting gradually. No specific injury."},
            {"speaker": "Provider", "text": "Where exactly on the knee do you feel it?"},
            {"speaker": "Patient", "text": "Inside part of my knee and underneath the kneecap. Worse when I bend it."},
            {"speaker": "Provider", "text": "Any swelling, redness, or warmth?"},
            {"speaker": "Patient", "text": "It swells up after basketball. Usually goes down by next day."},
            {"speaker": "Provider", "text": "Does the knee ever give way or lock up?"},
            {"speaker": "Patient", "text": "Sometimes it feels like it might buckle. And I hear popping or clicking sounds."},
            {"speaker": "Provider", "text": "How would you rate the pain daily?"},
            {"speaker": "Patient", "text": "Regular day maybe a 4, after basketball it's a 7 or 8."},
            {"speaker": "Provider", "text": "What have you been doing to treat it?"},
            {"speaker": "Patient", "text": "Ice packs, ibuprofen, and a knee brace from the pharmacy."},
            {"speaker": "Provider", "text": "Any family history of knee problems?"},
            {"speaker": "Patient", "text": "I'm 38. My dad had knee replacement at 60 for bad arthritis."},
            {"speaker": "Provider", "text": "How's your weight?"},
            {"speaker": "Patient", "text": "210 at 5'10. Gained about 20 pounds in the last two years."},
            {"speaker": "Provider", "text": "Let me examine the knee. We may need imaging."},
            {"speaker": "Patient", "text": "I just want to keep playing basketball if possible."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient reports right knee pain for six weeks limiting stair climbing."},
            {"line_idx": 3, "type": "detail", "summary": "Gradual onset from recreational basketball, no specific injury."},
            {"line_idx": 5, "type": "detail", "summary": "Pain localized to medial knee and under kneecap, worse with bending."},
            {"line_idx": 7, "type": "detail", "summary": "Post-exercise swelling that resolves by next day."},
            {"line_idx": 9, "type": "detail", "summary": "Knee buckling episodes and audible popping or clicking."},
            {"line_idx": 11, "type": "detail", "summary": "Baseline pain 4/10, increases to 7-8 after basketball."},
            {"line_idx": 13, "type": "detail", "summary": "Self-treating with ice, ibuprofen, and knee brace."},
            {"line_idx": 15, "type": "detail", "summary": "Age 38, father had knee replacement at 60 for arthritis."},
            {"line_idx": 17, "type": "detail", "summary": "210 lbs at 5'10, gained 20 pounds over two years."},
        ],
    },
    {
        "id": "case_09",
        "lines": [
            {"speaker": "Provider", "text": "What's the reason for your visit today?"},
            {"speaker": "Patient", "text": "I've developed this rash on my arms and torso about a week ago and it's really itchy and spreading."},
            {"speaker": "Provider", "text": "Where did it start?"},
            {"speaker": "Patient", "text": "My forearms, then spread to chest and stomach. Red raised bumps everywhere."},
            {"speaker": "Provider", "text": "Any new medications, soaps, or foods recently?"},
            {"speaker": "Patient", "text": "I started amoxicillin about 10 days ago for a urinary tract infection."},
            {"speaker": "Provider", "text": "Have you ever had a medication reaction before?"},
            {"speaker": "Patient", "text": "No, this is the first time."},
            {"speaker": "Provider", "text": "Any difficulty breathing or swelling of face or throat?"},
            {"speaker": "Patient", "text": "No, just the rash and itching."},
            {"speaker": "Provider", "text": "How bad is the itching?"},
            {"speaker": "Patient", "text": "Really bad especially at night. I'm scratching so much some spots are bleeding."},
            {"speaker": "Provider", "text": "Have you tried anything for it?"},
            {"speaker": "Patient", "text": "Hydrocortisone cream and Benadryl. Benadryl helps me sleep but the cream doesn't do much."},
            {"speaker": "Provider", "text": "Any fever or joint pain?"},
            {"speaker": "Patient", "text": "Low fever around 99 degrees and my joints have been achy."},
            {"speaker": "Provider", "text": "Any known allergies?"},
            {"speaker": "Patient", "text": "Just seasonal allergies to ragweed. No drug allergies that I know of."},
            {"speaker": "Provider", "text": "I'd like to stop the amoxicillin and switch antibiotics."},
            {"speaker": "Patient", "text": "Will the rash go away once I stop the medication?"},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient presents with spreading itchy rash on arms and torso for one week."},
            {"line_idx": 3, "type": "detail", "summary": "Rash started on forearms, spread to chest and stomach. Red raised bumps."},
            {"line_idx": 5, "type": "detail", "summary": "Started amoxicillin 10 days ago for urinary tract infection."},
            {"line_idx": 7, "type": "detail", "summary": "No prior medication reactions."},
            {"line_idx": 9, "type": "detail", "summary": "No anaphylaxis signs: no breathing difficulty or facial swelling."},
            {"line_idx": 11, "type": "detail", "summary": "Severe nocturnal itching causing excoriations from scratching."},
            {"line_idx": 13, "type": "detail", "summary": "Using hydrocortisone cream with minimal effect and Benadryl for sleep."},
            {"line_idx": 15, "type": "detail", "summary": "Low-grade fever of 99 degrees and joint achiness."},
            {"line_idx": 17, "type": "detail", "summary": "Known ragweed allergy, no known drug allergies."},
        ],
    },
    {
        "id": "case_10",
        "lines": [
            {"speaker": "Provider", "text": "What brings you in today?"},
            {"speaker": "Patient", "text": "I've been extremely tired for two to three months. No matter how much I sleep I wake up exhausted. And I've gained weight without changing my diet."},
            {"speaker": "Provider", "text": "How much weight have you gained?"},
            {"speaker": "Patient", "text": "About 15 pounds in the last three months with no changes in eating or exercise."},
            {"speaker": "Provider", "text": "How many hours of sleep are you getting?"},
            {"speaker": "Patient", "text": "Eight to 9 hours but I still need more. I could nap anytime during the day."},
            {"speaker": "Provider", "text": "Any changes in your skin, hair, or sensitivity to cold?"},
            {"speaker": "Patient", "text": "My skin is really dry and flaky. My hair seems thinner. And I'm always cold even when everyone else is comfortable."},
            {"speaker": "Provider", "text": "Any changes in mood or concentration?"},
            {"speaker": "Patient", "text": "I feel foggy and can't think clearly. I've been feeling down and not interested in things I usually enjoy."},
            {"speaker": "Provider", "text": "Any swelling in your face, hands, or feet?"},
            {"speaker": "Patient", "text": "My face looks puffy in the mornings. My rings are feeling tight."},
            {"speaker": "Provider", "text": "Any changes in your menstrual cycle?"},
            {"speaker": "Patient", "text": "My periods have been heavier and more irregular. They used to be very regular."},
            {"speaker": "Provider", "text": "Family history of thyroid problems?"},
            {"speaker": "Patient", "text": "My mother and sister both have hypothyroidism. My mom takes Synthroid."},
            {"speaker": "Provider", "text": "Any constipation?"},
            {"speaker": "Patient", "text": "Yes, I used to go every day and now it's every three days."},
            {"speaker": "Provider", "text": "I'd like to order thyroid function tests."},
            {"speaker": "Patient", "text": "That makes sense given my family history."},
        ],
        "annotations": [
            {"line_idx": 1, "type": "agenda_item", "summary": "Patient reports extreme fatigue for 2-3 months with unintentional weight gain."},
            {"line_idx": 3, "type": "detail", "summary": "15-pound weight gain over three months with no lifestyle changes."},
            {"line_idx": 5, "type": "detail", "summary": "Sleeping 8-9 hours but still exhausted with persistent daytime sleepiness."},
            {"line_idx": 7, "type": "detail", "summary": "Dry flaky skin, hair thinning, and cold intolerance."},
            {"line_idx": 9, "type": "detail", "summary": "Cognitive fog, difficulty concentrating, and depressed mood with anhedonia."},
            {"line_idx": 11, "type": "detail", "summary": "Morning facial puffiness and tight rings indicating fluid retention."},
            {"line_idx": 13, "type": "detail", "summary": "Heavier and more irregular menstrual periods."},
            {"line_idx": 15, "type": "detail", "summary": "Family history of hypothyroidism in mother and sister."},
            {"line_idx": 17, "type": "detail", "summary": "New onset constipation, decreased from daily to every three days."},
        ],
    },
]


def generate_sample_data(
    output_transcript_dir: str = "data/processed",
    output_annotation_dir: str = "data/annotations",
):
    """Generate 10 clinical conversation cases."""
    t_dir = Path(output_transcript_dir)
    a_dir = Path(output_annotation_dir)
    t_dir.mkdir(parents=True, exist_ok=True)
    a_dir.mkdir(parents=True, exist_ok=True)

    for f in t_dir.glob("*.json"):
        f.unlink()
    for f in a_dir.glob("*.json"):
        f.unlink()

    total_annotations = 0
    total_lines = 0

    for case in SAMPLE_CASES:
        transcript = {"id": case["id"], "lines": case["lines"]}
        with open(t_dir / f"{case['id']}.json", "w", encoding="utf-8") as f:
            json.dump(transcript, f, ensure_ascii=False, indent=2)

        annotations = {"id": case["id"], "annotations": case["annotations"]}
        with open(a_dir / f"{case['id']}.json", "w", encoding="utf-8") as f:
            json.dump(annotations, f, ensure_ascii=False, indent=2)

        total_annotations += len(case["annotations"])
        total_lines += len(case["lines"])

    print(f"Generated {len(SAMPLE_CASES)} clinical cases")
    print(f"  Total transcript lines: {total_lines}")
    print(f"  Total annotations: {total_annotations}")
    print(f"  Avg lines/case: {total_lines / len(SAMPLE_CASES):.1f}")
    print(f"  Avg annotations/case: {total_annotations / len(SAMPLE_CASES):.1f}")


if __name__ == "__main__":
    generate_sample_data()
