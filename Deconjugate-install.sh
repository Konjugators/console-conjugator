
#!/bin/bash
bold=" "

function install {
    if [[ "$(python3 -V)" =~ "Python 3" ]]; then
        echo "${bold}A proper version of python is installed, so installation will continue"
        echo "${bold}Click any key to continue"
        sudo apt-get install python3-pip
        echo "${bold}Pip has been updated/installed"
        echo "${bold}uninstalling previous versions"
        sudo python3 -m pip uninstall console-conjugator
        echo "${bold}installing latest version of console-conjugator"
        sudo python3 -m pip install console-conjugator/
        echo "${bold}testing proper installation:"
        konjugier machen er present
        echo "${bold}If the answer is er macht, the install has been succesful"
        echo "${bold}Click any key to continue"
        read varara
        echo "${bold}Removing source code"
        sudo rm -r console-conjugator/
        echo "${bold}Install script is complete, you can test it as such:"
        echo "${bold}konjugier infinitive pronoun tense"
    fi
}

function download {
    echo "${bold}Hello, and welcome to the installation guide."
    echo "${bold}Follow the instructions, and you can locally install the latest"
    echo "${bold}version of the console-conjugator, for german conjugation."
    echo "${bold}The first step is downloading: "
    echo "${bold}Would you like to download the source code? "
    read VARY
    if [[ "$VARY" = "yes" || ( "$VARY" = "y") || ( "$VARY" = "Y" ) ]]; then
        echo "${bold}Continuing download (note superuser priveleges may be necessary)"
        sudo git clone https://github.com/sandkoan/console-conjugator.git
        echo "${bold}Source code has been downloaded in $PWD/console-conjugator"
        echo "${bold}Downloading process is complete"
        install
    else
        echo "Aborting source code download"
        exit
    fi
}

download

