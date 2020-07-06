###############SNAKEMAKE################################

## conda install -c conda-forge mamba
## mamba create -c conda-forge -c bioconda -n snakemake snakemake

########################################################
import pandas as pd

configfile: "config.yaml"

samples_names = config["samples_names"]

samplesID=pd.read_table(samples_names)['names']
barcodesID=pd.read_table(samples_names)['Barcodes']

rule all:
    input:
        "qualityC/pycoQC_output_min_pass_q10.html"

rule qualityC:
    input:
        "sequencing_summary.txt"
    output:
        "qualityC/pycoQC_output_min_pass_q10.html"
    threads: 8
    log:
        "logs/qualityC/pycoQC.log"
    conda:
        "/home/hirondelle/miniconda3/envs/pycoqc.yaml"
    shell:
        "pycoQC  --summary_file {input} --html_outfile {output} --min_pass_qual 10 2> {log}"

rule rename:
    input:

    output:

    shell:
        mv data/{input.before}.fastq.gz data/{output.after}.fastq.gz
