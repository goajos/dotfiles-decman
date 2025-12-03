#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# run decman with the correct source file
alias decman='decman --source /home/jappe/Repositories/dotfiles/source.py'
alias vim='nvim'

function yay()
{
  if [ $# -eq 0 ]; then
    # update system
    paru -Syu
  else
    # install aur package
    paru -S -- "$@"
  fi
}

function yeet()
{
  if [ $# -eq 0 ]; then
    # clean cache
    paru -Scc
  else
    # remove aur package
    paru -Rns -- "$@"
  fi
}

# uv
export PATH="/home/jappe/.local/bin:$PATH"
