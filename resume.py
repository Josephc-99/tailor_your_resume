from docx import Document
import openai
import PyPDF2

openai.api_key = "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"


# Function to make the ChatGPT API call
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=[prompt],  # Pass the prompt as a list
        temperature=0.3,
        max_tokens=1000,
        n=1,
        stop=None,
    )
    return response.choices[0]['text'].strip()

# Function to read the existing resume from a file
def read_resume(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        resume_text = []
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            resume_text.append(page.extract_text())
    return '\n'.join(resume_text)

# Function to write the revised resume to a new file
def write_revised_resume(file_path, revised_resume):
    doc = Document()
    doc.add_paragraph(revised_resume)
    doc.save(file_path)

# Main function
def main():
    existing_resume_path = 'C:\\Users\\yusuf\\codeProjects\\resume.pdf'
    existing_resume_text = read_resume(existing_resume_path)
    new_resume_text_path = 'C:\\Users\\yusuf\\Downloads\\Untitled document.pdf'
    new_resume_text = read_resume(new_resume_text_path)

    # Get the LinkedIn job post from the user
    # linkedin_job_post = input("Enter the LinkedIn job post details:\n")

    # Combine existing resume and job post as a prompt for ChatGPT
    prompt = f"This is my default resume showcasing skills and experience:{existing_resume_text}. Please write me a new resume tailored for the following job post:\nJob Post Details:\n{new_resume_text}"

    # Call the ChatGPT API to generate the revised resume
    revised_resume = generate_response(prompt)

    # Save the revised resume to a new file with a proper filename
    revised_resume_path = 'revised_resume.docx'
    write_revised_resume(revised_resume_path, revised_resume)

    print("Revised resume has been generated and saved as 'revised_resume.docx'.")

if __name__ == "__main__":
    main()