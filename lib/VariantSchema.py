#!/usr/bin/env python
#encoding=utf-8

class VariantSchema:
    
    strand = {
        "+": "POS_STRAND",
        "-": "NEG_STRAND"
    };

    # A Position is an unoriented base in some Reference
    class Position:
        # (string) – The name of the Reference on which the Position is located.
        referenceName = "";
        
        # The 0-based offset from the start of the forward strand for that Reference.
        position = 0;
        
        # (Strand) – Strand the position is associated with.
        strand = None;
     
    # Identifier from a public database   
    class  ExternalIdentifier:
        # The source of the identifier. e.g. Ensembl
        database = "";
        
        # The ID defined by the external database. e.g. ENST00000000000
        identifier = "";
        
        # The version of the object or the database. e.g. 78
        version = 1;
    
    # Optional metadata associated with a variant set.
    class  VariantSetMetadata:
        # (string) – The top-level key.
        key = "";
        
        # (string) – The value field for simple metadata.
        value = "";
        
        # (string) – User-provided ID field, not enforced by this API.
        id = "";
        
        # (string) – The type of data.
        type = "";
        
        # (string) – The number of values that can be included in a field described by this metadata
        number = 0;
        
        # (string) – A textual description of this metadata.
        description = "";
        
         # (map<array<string>>) – Remaining structured metadata key-value pairs.
        info = {};
    
    # A VariantSet is a collection of variants and variant calls intended to be analyzed together.    
    class VariantSet:
        # (String) - The variant set ID
        id = "";
        
        # (null|String) - The variant set name. e.g. NA12878
        name = None;
        
        # (String) - The ID of dataset this variant belongs to 
        datasetId = "";
        
        # (string) - The ID of the reference set that describes the sequence used by this variant in this sets.
        referenceSetId = "";
        
        # (array<VariantSetMetadata>) - Optional metadata associated with this variant set.
        metadata = [];
    
    class CallSet:
        id = "";
        
        name = None;
        
        sampleID = None;
        
        variantSetIds = [];
        
        created = None;
        
        updated = None;
        
        info = None;
    
    # A Call represents the determination of genotype with respect to a particular Variant
    class Call:
        # (null|string) - The name of the call set this variant call belongs to.
        callSetName = None;
        
        #  (null|string) – The ID of the call set this variant call belongs to
        callSetId = None;
        
        # (array<int>) - The genotype of this variant call
        genotype = [];
        
        # (null|string) - If this field is not null, this variant call’s genotype ordering implies
        phaseset = None;
        
        # (array<double>) - The genotype likelihoods for this variant call. Each array entry
        genotypeLikelihood = [];
        
        # (map<array<string>>) - A map of additional variant call information.
        info = None;
        
    # A Variant represents a change in DNA sequence relative to some reference. 
    class Variant:
        # (String) - The variant ID
        id = "";
        
        # (String) - The ID of variant set this variant belongs to.
        variantSetId = "";
        
        # (array<String>) - Names for the variant. e.g. RefSNP ID
        names = [];
        
        # (null|long) - The date this variant was created in milliseconds from the epoch.
        created = None;
        
        # (null|long) - The date this variant was updated in milliseconds from the epoch.
        updated = None;
        
        # (string) - The reference on which this variant occurs. e.g. chr20
        referenceName = "";
        
        # (long) - The start position at which this variant occurs (0-based).
        start = None;
        
        # (long) - The end position (exclusive), resulting in [start, end) closed-open interval.
        end = None;
        
        # (string) - The reference bases for this variant. They start at the given start position.
        referenceBases = None;
        
        # (array<String>) - The bases that appear instead of the reference bases. Multiple alternate
        alternateBases = [];
        
        # (map<array<string>>) – A map of additional variant information.
        info = None;
        
        # (array<Call>) – The variant calls for this particular variant. Each one represents the determination of genotype with respect to this variant. Call`s in this array are implicitly associated with this `Variant. 
        calls = None;