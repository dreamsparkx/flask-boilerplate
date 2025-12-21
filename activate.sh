if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "This script must be sourced, not executed." 
    echo "Try: source ./activate.sh"
    exit 1
fi

. venv/bin/activate