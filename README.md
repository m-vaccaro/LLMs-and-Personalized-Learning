# LLMs-and-Personalized-Learning

Use of the codes, files, or paragraphs presented here in any future works must reference the latest published version of the paper by Vaccaro, Friday, and Zaghi.

------
This respository contains the code needed to run the experiment through the custom-designed graphical user interface (GUI). It also contains the paragraphs used in each of the text pairs for the training and test sessions in a .PDF file.

The ExperimentGUI folder contains the following:
- A folder of icons (.png) images that are used in the GUI.
- input_paragraphs.csv contains the text of the first four paragraph pairs used in the experiment. References with weblinks to the original Wikipedia articles for the source texts are available in the TrainingAndTestSessionParagraphs.PDF file.
- instructions.txt contains the instructions shown to participants on the main screen of the GUI.
- openai_interact_profile.py and openai_interact_rewrite.py define the PROFILER and REWRITE GPT-4 models referenced in Figure 1 of the paper, respectively. Each of these codes contains the relevant User and System message(s) that define the behavior of each model.
- GUI.py is the main code for the graphical user interface. This code references the Icons folder, input_paragraphs.csv, instructions.txt, openai_interact_profile.py, and openai_interact_rewrite.py. These files must be in the same directory for this code to run properly.
- Note that running the code (without modifications) will require you to have an OpenAI API key.
