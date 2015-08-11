#! /bin/sh
#
pmdatadir="../data/"
pmdataufile="u.data"
#
gplt="../bin/gplot.csh"
#
echo "---"
echo ""
echo "The few first lines of the file"
echo ""
head ${pmdatadir}${pmdataufile}
echo ""
echo "---"
echo "Note the format:"
echo "UsedID MovieID Rating Timestamp"
echo ""
echo "---"
#
echo ""
echo "Counting...   with: wc ${pmdatadir}${pmdataufile}"
echo ""
wc ${pmdatadir}${pmdataufile}
echo ""
echo "Lines:" `wc -l ${pmdatadir}${pmdataufile}`
echo "Words:" `wc -w ${pmdatadir}${pmdataufile}`
echo "Chars:" `wc -m ${pmdatadir}${pmdataufile}`
echo "Bytes:" `wc -c ${pmdatadir}${pmdataufile}`
echo "Chars:" `cat ${pmdatadir}${pmdataufile} | sed 's/ //g' | sed 's/\t//g' | wc -m`
#
echo ""
echo "---"
#
echo ""
echo "Number of Users"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $1;}' | sort -n | uniq | wc -l
#
echo ""
echo "---"
#
echo ""
echo "Number of Movies"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $2;}' | sort -n | uniq | wc -l
#
echo ""
echo "---"
#
echo ""
echo "Number of Ratings: Rating scale."
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $3;}' | sort -n | uniq | wc -l
#
echo ""
echo "---"
#
echo ""
echo "Number of Timestamps: same time rating?"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $4;}' | sort -n | uniq | wc -l
echo " -- Note concurrent time stamps"
echo "---"
#
echo ""
echo "---"
#
echo ""
echo "Vote distribution per Users"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $1;}' | sort -n | uniq -c | awk '{print $1;}' | sort -nr | nl > x.$$.uvd
${gplt} x.$$.uvd
rm x.$$.uvd
#
