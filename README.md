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
  <li> Program is simply run using command (use tab key for autocompletion):  <code> (python - windows, python3 - linux or mac os) run_caesar.py (text file) (key: 0 - 25) (ciphering option: ‘e’ or ‘d’)</code></li>
  <li>To avoid loss of original information from the text file, extra exceptions are raised such that the users enter the parameters correctly in CLI</li>
</ul>

## Demo - Running run_caesar.py program

<ol>
  <li>Open terminal or powershell in the directory where program, its dependencies and the text file to be ciphered are located</li>
  <p align="center">
  <br><img src="https://user-images.githubusercontent.com/20547074/53670743-347e5900-3c95-11e9-99a9-f57f65b9d360.png">
  <br><p align="center"><strong><i>Figure 1</i></strong>: Terminal opened in the working directory</p>
  </p>
  <p align="center">
  <img src="https://user-images.githubusercontent.com/20547074/53672187-d0f72a00-3c9a-11e9-802b-644524a0d0b6.png">
  <br><p align="center"><strong><i>Figure 2</i></strong>: Text file before its encryption</p>
  </p>
  <li>To encrypt the file, type command: <code> python3 run_caesar.py message.txt 20 e</code></li>
  <p align="center">
  <br><img src="https://user-images.githubusercontent.com/20547074/53672188-d18fc080-3c9a-11e9-96b7-0e584688d61a.png">
  <br><p align="center"><strong><i>Figure 3</i></strong>: Text file after successful encryption. Each of the letters are shifted to the right by 20</p>
  </p>
  <li>To get back original text file (decryption): <code> python3 run_caesar.py message.txt 20 d</code></li>
</ol>

## Resources
1 Design of Computer Programs | Udacity. 2019. Design of Computer Programs | Udacity. [ONLINE] Available at: https://www.udacity.com/course/design-of-computer-programs--cs212. [Accessed 01 March 2019].

2 3.7.2 Documentation. 2019. 3.7.2 Documentation. [ONLINE] Available at: https://docs.python.org/3/. [Accessed 01 March 2019].

