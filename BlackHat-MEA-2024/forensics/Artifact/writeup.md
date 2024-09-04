# Artifact - forensics


## Description

During the investigation of a compromised machine, it was determined that an impersonation tool had been executed. The Digital Forensics and Incident Response (DFIR) team has provided only a specific hive for analysis. Your objective is to identify the name of the executable associated with the impersonation tool and determine the earliest suspected execution time of this executable on the affected machine. Flag format/example: BHFlagY{cmd.exe_29/12/1992_22:33:13}

## Solution

- We have been given a hive file, which is the file responsible for storing Windows registries.
There are many hive files on Windows (such as SOFTWARE, SYSTEM, etc.), so the first thing we need to do is identify which one we have. The best tool for parsing hive files is `regripper`. We can use it as follows to learn about the hive file: `regripper -r execution -g` -> `System`.

- The System hive has many registry keys that hold information about running processes or executed commands. 
The most famous ones are for `AppCompatCache`.
Regripper has a plugin that can parse this registry directly: `regripper -r execution -p appcompatcache`.

- Many processes can be found in the output, listed by their image filenames and execution times. The 
interesting ones are those executed from the User folder (e.g. Downloads or Desktop), as 
malware often starts from there.

- One listed process stands out as potentially malicious (though we can't be sure, based on its suspicious name, location, and the challenge description): `C:\Users\Labib\Desktop\AmcacheParser\DeadPotato-NET4.exe  2024-08-09 22:42:13`.
