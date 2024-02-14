#!/bin/sh
curl "https://github.com/wxMaxima-developers/wxmaxima/releases" 2>/dev/null |grep "tag/Version-" |sed -e 's,.*tag/Version-,,;s,\".*,,;' |head -n1

