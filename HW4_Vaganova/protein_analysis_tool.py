from typing import List, Union

# 3-latter with corresponding 1-letter residues names
RESIDUES_NAMES = {'ALA': 'A',
                  'ARG': 'R',
                  'ASN': 'N',
                  'ASP': 'D',
                  'CYS': 'C',
                  'GLN': 'Q',
                  'GLU': 'E',
                  'GLY': 'G',
                  'HIS': 'H',
                  'ILE': 'I',
                  'LEU': 'L',
                  'LYS': 'K',
                  'MET': 'M',
                  'PHE': 'F',
                  'PRO': 'P',
                  'SER': 'S',
                  'THR': 'T',
                  'TRP': 'W',
                  'TYR': 'Y',
                  'VAL': 'V'
                  }

# first value is hydrophobicity index, second is pKa (pKa1, pKa2, pKa3 respectively), third is molecular mass in Da
RESIDUES_CHARACTERISTICS = {'A': [1.8, [2.34, 9.69, 0], 89],
                            'R': [-4.5, [2.17, 9.04, 12.48], 174],
                            'N': [-3.5, [2.02, 8.80, 0], 132],
                            'D': [-3.5, [1.88, 9.60, 3.65], 133],
                            'C': [2.5, [1.96, 10.28, 8.18], 121],
                            'Q': [-3.5, [2.17, 9.13, 0], 146],
                            'E': [-3.5, [2.19, 9.67, 4.25], 147],
                            'G': [-0.4, [2.34, 9.60, 0], 75],
                            'H': [-3.2, [1.82, 9.17, 6.00], 155],
                            'I': [4.5, [2.36, 9.60, 0], 131],
                            'L': [3.8, [2.36, 9.60, 0], 131],
                            'K': [-3.9, [2.18, 8.95, 10.53], 146],
                            'M': [1.9, [2.28, 9.21, 0], 149],
                            'F': [2.8, [1.83, 9.13, 0], 165],
                            'P': [-1.6, [1.99, 10.60, 0], 115],
                            'S': [-0.8, [2.21, 9.15, 0], 105],
                            'T': [-0.7, [2.09, 9.10, 0], 119],
                            'W': [-0.9, [2.83, 9.39, 0], 204],
                            'Y': [-1.3, [2.20, 9.11, 0], 181],
                            'V': [4.2, [2.32, 9.62, 0], 117]}

AMINO_ACID_TO_MRNA = {'A': 'GCN',
                      'R': '(CGN/AGR)',
                      'N': 'AAY',
                      'D': 'GAY',
                      'C': 'UGY',
                      'Q': 'CAR',
                      'E': 'GAR',
                      'G': 'GGN',
                      'H': 'CAY',
                      'I': 'AUH',
                      'L': '(CUN/UUR)',
                      'K': 'AAR',
                      'M': 'AUG',
                      'F': 'UUY',
                      'P': 'CCN',
                      'S': '(UCN/AGY)',
                      'T': 'ACN',
                      'W': 'UGG',
                      'Y': 'UAY',
                      'V': 'GUN'}

def change_residues_encoding(seq: str, query: str = 'three') -> str:
    """
    Transfer amino acids from 3-letter to 1-letter code and vice versa. By default, converts all seq into 1-letter
    format, even those already 1-letter. Case-sensitive.
    :param seq: protein seq (str) :param query: specify current encoding (str)
    :return: same protein seq in another encoding (str)
    """
    pass


def is_protein(seq: str) -> bool:
    """
    Identify invalid seq elements, which are not presented in dicts above
    :param seq: protein seq in 1-letter encoding (str)
    :return: if seq is correct protein seq or not (bool)
    """
    return True


def get_seq_characteristic(seq: str) -> dict:
    """
    Count entry of each residue type in your seq. Get description of amino acid composition.
    :param seq: protein seq in 1-letter encoding (str)
    :return: each residue type in seq in 3-letter code and its amount in current seq (dict)
    """
    res_count = {}
    for res in seq:
        res_count[[tl_code for tl_code in RESIDUES_NAMES if RESIDUES_NAMES[tl_code] == res][0]] = 0
    for res in seq:
        res_count[[tl_code for tl_code in RESIDUES_NAMES if RESIDUES_NAMES[tl_code] == res][0]] += 1
    return res_count


def find_res_in_seq(seq: str, res: str) -> str:
    """
    Find all positions of certain residue in your seq
    :param seq: protein seq in 1-letter encoding (str)
    :param res: specify the residue of interest (str)
    :return: positions of specified residue in your seq (str)
    """
    res_of_interest_position = []
    for ind, res in enumerate(res_seq, 1):
        if res == res_of_interest:
            res_of_interest_position.append(ind)
    return f'{res_of_interest} positions: {res_of_interest_position}'


def find_site(seq: str, site: str) -> str:
    """
    Find if seq contains certain site and get positions of its site
    :param seq: protein seq in 1-letter encoding (str)
    :param site: specify site of interest as short seq in 1-latter code (str)
    :return: positions of residues for each certain site in seq (str)
    """
    if seq not in RESIDUES_NAMES.values():
        raise ValueError(f'{site} site is not a protein sequence!')
    if site in seq:
        site_full_coordinates = []
        site_count = seq.count(site)
        site_start_coordinates = [coordinate for coordinate in range(len(seq)) if seq.startswith(site, coordinate)]
        site_end_coordinates = [(coordinate + len(site)) for coordinate in site_start_coordinates]
        for counter in range(len(site_start_coordinates)):
            site_full_coordinates.append([site_start_coordinates[counter], site_end_coordinates[counter]])
        if site_count == 1:
            return f'{site} found in sequence {site_count} time; site coordinates are {site_full_coordinates}'
        else:
            return f'{site} found in sequence {site_count} times; site coordinates are {site_full_coordinates}'
    else:
        raise ValueError(f'{site} site is not in sequence!')


def calculate_protein_mass(seq: str) -> float:
    """
    Get mass of residues in your seq in Da
    :param seq: protein seq in 1-letter encoding (str)
    :return: mass in Da (float)
    """
    total_mass = 0
    for res in seq:
        total_mass += RESIDUES_CHARACTERISTICS[res][2]
    return total_mass


def calculate_average_hydrophobicity(seq: str) -> float:
    """
    Get hydrophobicity index for protein seq as sum of index for each residue in your seq divided by its length
    :param seq: protein seq in 1-letter encoding (str)
    :return: average hydrophobicity (float)
    """
    sum_hydrophobicity_ind = 0
    for res in seq:
        sum_hydrophobicity_ind += RESIDUES_CHARACTERISTICS[res][0]
    return sum_hydrophobicity_ind / len(seq)


def get_mrna(seq: str) -> str:
    """
    Get encoding mRNA nucleotides for your seq
    :param seq: protein seq in 1-letter encoding (str)
    :return: potential encoding mRNA sequences with multiple choice for some positions (str)
    """
    mrna_seq = str()
    for res in amino_acid_seq:
        mrna_seq += AMINO_ACID_TO_MRNA[res]
    return mrna_seq


def calculate_isoelectric_point(seq: str) -> float:
    """
    Find isoelectrinc point as sum of known pI for residues in your seq
    :param seq: protein seq in 1-letter encoding (str)
    :return: isoelectric point (float)
    """
    sum_pka = 0
    pka_amount = 0
    for ind, res in enumerate(seq, 1):
        if ind == 1:
            sum_pka += RESIDUES_CHARACTERISTICS[res][1][1]
            pka_amount += 1
        elif RESIDUES_CHARACTERISTICS[res][1][2] != 0:
            sum_pka += RESIDUES_CHARACTERISTICS[res][1][2]
            pka_amount += 1
        elif ind == len(seq):
            sum_pka += RESIDUES_CHARACTERISTICS[res][1][0]
            pka_amount += 1
    pi = sum_pka / pka_amount
    return pi


def run_protein_analysis(*args: str) -> Union[List[str], str]:
    """
    Launch desired operation with proteins sequences. Pass comma-separated sequences,
    additional argument (if certain function requires it) and specify function name you want to apply to all sequences.
    Pass arguments strictly in this order, otherwise it won't be parsed.

    :param args:
    - seq (str): amino acids sequences for analysis in 1-letter or 3-letter code (as many as you wish)
    - additional arg (str): necessary parameter for certain functions (for example, specify target protein site)
    - operation name (str): specify procedure you want to run

    :return: the result of procedure in list or str format
    """

    # first value is function callable name, second is real function, third is number of function arguments
    function_names = {'change_residues_encoding': [change_residues_encoding, 2],
                      'get_seq_characteristic': [get_seq_characteristic, 1],
                      'find_res_in_seq': [find_res_in_seq, 2],
                      'find_site': [find_site, 2],
                      'calculate_protein_mass': [calculate_protein_mass, 1],
                      'calculate_average_hydrophobicity': [calculate_average_hydrophobicity, 1],
                      'get_mrna': [get_mrna, 1],
                      'calculate_isoelectric_point': [calculate_isoelectric_point, 1]}

    procedure = args[-1]

    processed_result = []

    seqs = [change_residues_encoding(seq.upper()) for seq in args[:-1 * (function_names[procedure][1])]]
    for idx, seq in enumerate(seqs):
        if not is_protein(seq):
            print(f'Sequence number {idx + 1} is not available for operations! Skip it.')
            continue
        if function_names[procedure][1] == 1:
            processed_result.append(function_names[procedure][0](seq))
        elif function_names[procedure][1] == 2:
            add_arg = args[-2].upper()
            processed_result.append(function_names[procedure][0](seq, add_arg))
    if len(processed_result) == 1:
        return processed_result[0]
    return processed_result
