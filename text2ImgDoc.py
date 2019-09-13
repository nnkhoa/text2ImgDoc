import os, sys, codecs, subprocess, csv
import justext

def txt_to_img(txtfile, output):
    with codecs.open(txtfile, 'r', 'utf-8') as f:
        text = f.read().strip()
    
    text_raw = remove_boilerplate(text)
    
    command = 'convert -size 1240x -fill black -pointsize 24 -fill black'.split(' ')

    command.append('caption:' + text_raw)
    command.append(output)

    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = p.communicate()

    if p.returncode != 0:
        output_error(txtfile, "log")

def output_error(txtfile, log_file):
    f = open(log_file, "a+")
    f.write(txtfile + '\n')
    f.close()

def remove_boilerplate(text):
    paragraphs = justext.justext(text, justext.get_stoplist('English'), length_low = 5)
    
    output = ''

    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            output += paragraph.text + '\n'
    
    return output

def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
        print("Directory " + dir_name + " created")
    except FileExistsError:
        print("Directory " + dir_name + " existed")

def convert_files(in_dir, out_dir):
    for doc_file in os.listdir(in_dir):
        print(doc_file)
        if doc_file == ".DS_Store":
            continue
        infile = os.path.abspath(in_dir) + "/" + doc_file
        outfile = os.path.abspath(out_dir) + "/" + doc_file + ".png"
        txt_to_img(infile, outfile)

def walk_through_dir(in_dir, main_out_dir):
    for (dir_path, dir_names, file_names) in os.walk(in_dir):
        if len(dir_names) > 0:
            for dir_name in dir_names:
                out_dir = main_out_dir + "/" + dir_path + "/" + dir_name
                if not os.path.exists(out_dir):
                    create_dir(out_dir)
        else:
            print(dir_path, len(dir_names))
            out_dir = main_out_dir + "/" + dir_path
            print(out_dir, dir_path)
            convert_files(dir_path, out_dir)

def create_output_dir(in_dir, main_out_dir):
    for(dir_path, dir_names, file_names) in os.walk(in_dir):
        if len(dir_names) > 0:
            for dir_name in dir_names:
                out_dir = main_out_dir + "/" + dir_name

def main():
    doc_dir = sys.argv[1]
    main_out_dir = sys.argv[2]
    
    create_dir(main_out_dir)
    create_dir(main_out_dir + "/" + doc_dir)
    
    if os.path.exists(doc_dir):
        walk_through_dir(doc_dir, main_out_dir)
        # for doc_file in os.listdir(doc_dir):
        #     infile = os.path.abspath(doc_dir) + "/" + doc_file
        #     outfile = os.path.abspath(out_dir) + "/" + doc_file + ".png"
        #     txt_to_img(infile, outfile)

if __name__ == "__main__":
    main()
