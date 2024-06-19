import os
import markdown


def read_md_file(file):
  with open(file, 'r') as f:
    return f.read()

def md_to_html(md_file):
  html = markdown.markdown(md_file)
  return html

def write_html_file(file,html_file):
  with open(file,'w')as f:
    f.write(html_file)

def main():
  md_file_path = 'simple.md'
  html_file_path = 'test.html'

  if not os.path.exists(md_file_path):
    print(f"Error: {md_file_path} does not exist.")

  md_file= read_md_file(md_file_path)
  print("markdown file raed succesfully")
  html_file= md_to_html(md_file)
  print("html file created succesfully")
  write_html_file(html_file_path, html_file)
  print(f"Html content written to {html_file_path}")

if __name__ == 'main':
  main()
