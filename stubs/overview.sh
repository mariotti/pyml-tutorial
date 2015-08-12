#! /bin/sh
#
pmdatadir="../data/"
pmdataufile="u.data"
#
gplt="../bin/gplot.csh"
#dogplt="gplot"
dogplt="NOgplot"
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
echo "Number of votes distribution per each Users (anonymized)"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $1;}' | sort -n | uniq -c | awk '{print $1;}' | sort -nr | nl > x.$$.uvud
echo "Number of votes of the highest voter: " `head -1 x.$$.uvud`
if [ ${dogplt} == "gplot" ];
then
    ${gplt} x.$$.uvud
    rm x.$$.uvud
fi
#
echo ""
echo "---"
#
echo ""
echo "Number of votes distribution per user"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $1;}' | sort -n | uniq -c | awk '{print $1;}' | sort -n | uniq -c | awk '{print $2,$1;}' > x.$$.uvtd
if [ ${dogplt} == "gplot" ];
then
    ${gplt} x.$$.uvtd
    rm x.$$.uvtd
fi
#
#
echo ""
echo "---"
#
echo ""
echo "Number of votes distribution per each Movie (anonymized)"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $2;}' | sort -n | uniq -c | awk '{print $1;}' | sort -nr | nl > x.$$.mvmd
echo "Number of votes of the highest voted movie: " `head -1 x.$$.mvmd`
if [ ${dogplt} == "gplot" ];
then
    ${gplt} x.$$.mvmd
    rm x.$$.mvmd
fi
#
echo ""
echo "---"
#
echo ""
echo "Number of votes distribution per movie"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $2;}' | sort -n | uniq -c | awk '{print $1;}' | sort -n | uniq -c | awk '{print $2,$1;}' > x.$$.mvtd
if [ ${dogplt} == "gplot" ];
then
    ${gplt} x.$$.mvtd
    rm x.$$.mvtd
fi
#
echo ""
echo "---"
#
echo ""
echo "Rating Distribution"
echo ""
cat ${pmdatadir}${pmdataufile} | awk '{print $3;}' | sort -n | uniq -c | awk '{print $2,$1;}' > x.$$.rtd
if [ ${dogplt} == "gplot" ];
then
    ${gplt} x.$$.rtd
    rm x.$$.rtd
fi
#
###############################
###############################
#
# Prepare CSV
cat ${pmdatadir}${pmdataufile} | sort -n -k 1,1 -k 2,2 | awk '{printf("%s,%s,%s,%s\n",$1,$2,$3,$4);}' > u.csv


#
##############################
##############################
rm x.*
#
