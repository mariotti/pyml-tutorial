#! /bin/tcsh
#
if ("a$1" == "a") then
  echo "give a file name..."
  exit
endif
if ("a$1" == "ahelp") then
  echo "Usage: $0  <datafilename> [numcols]"
  echo ""
  exit
endif
if ("a$2" == "a") then
set numcols=2
else
set numcols=$2
endif
#
#
# @ numcols = $numcols + 1
set cnum=2
set pltcmd="plot '$1' using 1:2"
while ( $cnum != $numcols )
@ cnum = $cnum + 1
set pltcmd="${pltcmd}, '$1' using 1:${cnum}"
end
#
echo "Plot cmd: $pltcmd"
#
cat << EOF > x.plot.$$
set style data linespoints
$pltcmd
pause -1 "Hit return to continue"
EOF
#
gnuplot x.plot.$$
#
rm x.plot.$$
#
