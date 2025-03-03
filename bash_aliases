export GIT_PS1_SHOWDIRTYSTATE=1

branch_icon='\ue725'
file_icon='\uf07b'

PS1_TEMP=$'\n\[\033[38;5;147m\]\uf07b \u \w\[\033[38;5;208m\]$(__git_ps1 " |$branch_icon %s |")\[\033[01;00m\]\n\u276f_>export PS1=$PS1_TEMP

mem() {
    if [ "$1" == "stash" ]; then
        export MY_MEM=$(pwd);
        echo "Saved directory!";
    elif [ "$1" == "pop" ]; then
        cd $MY_MEM;
    elif [ "$1" == "ls" ]; then
        echo "Saved directory: $MY_MEM";
    else
        echo "Use mem stash or mem pop!";
    fi
}
