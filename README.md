<p align="center">
  <img src="https://user-images.githubusercontent.com/20547074/53671483-fdf60d80-3c97-11e9-9f99-3a8e6ba76dcf.png">
</p>

# Caesar Cipher - Python Implementation

Program implemented using Python for ciphering - encryption or decryption of a raw text file.

## Files
<ul> 
  <li> <code>cipher.py</code> - Python module which includes class Cipher. It consists of all functions and methods that allows to cipher the file.
  </li>
  <li> <code>run_caesar.py</code> - Python file which allows ciphering of the files from command line interface (CLI) - terminal (Linux and Mac OX) and powershell (Windows).
  </li>
  <li> <code>message.txt</code> - Text file to be ciphered. Other text files with different names can be used for ciphering as  <code>run_caesar.py</code> will take the text filename as input from CLI.
  </li>
</ul>

## Notes

<ul>
  <li> To check theoretical details of Caesar Cipher: https://en.wikipedia.org/wiki/Caesar_cipher </li>
  <li> Program is simply run using command (use tab key for autocompletion):  <code> 'python - windows, python3 - linux or mac os' run_caesar.py 'text file' 'key value - 0 - 25' '‘e’ or ‘d’'</code></li>
</ul>

## Demo - Running run_caesar.py program

<ol>
  <li>Open terminal or powershell in the directory where program, its dependencies and the text file to be ciphered are located.</li>
  <img src="https://user-images.githubusercontent.com/20547074/53670743-347e5900-3c95-11e9-99a9-f57f65b9d360.png">
  <li>To encrypt the file, type command: <code> python3 run_caesar.py message.txt 20 e </code>. File after encryption shown in <i>Figure 3</i></li>
  <li>To get back original text file (decryption): <code> python3 run_caesar.py message.txt 20 d </code></li>
</ol>

