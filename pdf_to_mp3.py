import pyttsx3, pypdf

# Ask the user for the PDF file name and the desired MP3 file name
pdf_file_name = input("Enter the name of the PDF file (with .pdf extension): ")
mp3_file_name = input("Enter the desired name for the MP3 file (with .mp3 extension): ")

pdfreader = pypdf.PdfReader(open(pdf_file_name, 'rb'))
speaker = pyttsx3.init()
clean_text = ''

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text += text.strip().replace('\n', '')

print(clean_text)

# Set the rate (you can adjust the value to be higher or lower as per your preference)
new_rate = 150  # Setting a slower rate than usual
speaker.setProperty('rate', new_rate)

speaker.save_to_file(clean_text, mp3_file_name)
speaker.runAndWait()

speaker.stop()
