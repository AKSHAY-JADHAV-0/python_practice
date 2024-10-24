#Write a program to detect double space in a string.
#paragraph = "In the modern  era of technology, cloud  computing has revolutionized the way businesses operate. It offers scalable resources, enabling companies to manage  their infrastructure  more efficiently. From data storage to application deployment, cloud platforms provide a flexible and cost-effective solution for organizations of all sizes. As companies continue to adopt cloud services, the demand for skilled professionals in cloud computing, DevOps, and data engineering has skyrocketed. These experts play a critical role in ensuring the seamless integration and operation of cloud-based systems, driving innovation and productivity in today's competitive market."

paragraph = str(input("Enter ypur paragraph: "))
paragraph_find = paragraph.find(" ","color_space=True{'r'}")
Highlight_paragraph = paragraph_find
print(f"spaces in paragraph: ",paragraph_find = ("color_space=True{'r'}"))
#print(f"\nenter spaces in string:",paragraph_find(sort_colors=True,colors=('r')))
#highlighted_paragraph = paragraph.replace ("  "," ","\033[91m  \033[0m")
#double_spaced_paragraph = paragraph.replace("  ", " ")
#print(double_spaced_paragraph)

