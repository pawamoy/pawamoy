#!/usr/bin/env bash
if [ "$1" != "pawamoy" ]; then
    prefix="$1/"
fi
gh repo list "$1" \
    --source \
    --visibility public \
    --json name \
    -q '.[]|.name' |
        sed "s#^#[${prefix}#;s#\$#](https://github.com/$1/)#" |
        sort
