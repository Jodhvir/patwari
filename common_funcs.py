def calculate_individual_share(measurement_type,value1,value2,value3,ratio_nr,ratio_dr):
    if measurement_type == 'Bigha/Biswa':
        total_area_biswasi = (value1*400) + (value2*20) + value3

        # Calculate individual share in biswasiyan
        INDIVIDUAL_SHARE_BISWASIYAN = total_area_biswasi * ratio_nr / ratio_dr 

        FINAL_BIGHA, FINAL_BISWA,FINAL_BISWASI = biswasiyan_to_bbb(INDIVIDUAL_SHARE_BISWASIYAN)
        return [FINAL_BIGHA, FINAL_BISWA,FINAL_BISWASI]  


    else:
        total_area_sarsahi = (value1*180) + (value2*9) + value3

        # Step 1: Calculate individual share in SARSAHIyan
        INDIVIDUAL_SHARE_SARSAHIYAN = total_area_sarsahi * ratio_nr / ratio_dr 

        FINAL_KANAL, FINAL_MARLA,FINAL_SARSAHI = convert_sarsahi_to_kms(INDIVIDUAL_SHARE_SARSAHIYAN)
        return[FINAL_KANAL, FINAL_MARLA,FINAL_SARSAHI]

        

# ---------------------------------------
# Add or Subtract Land based on Selection
# ---------------------------------------
def land_add_subtract(measurement_type,value1,value2,value3,value4,value5,value6,add_or_subtract):
    if measurement_type == 'Bigha/Biswa':
        total_area_biswasi = (value1*400) + (value2*20) + value3

        total_area_add_subtract = (value4*400) + (value5*20) + value6

        if add_or_subtract == 'Add':
            total_area_biswasi = total_area_biswasi + total_area_add_subtract
        else:
            total_area_biswasi = total_area_biswasi - total_area_add_subtract
        
        # Find Bigha, Biswa, Biswasi
        FINAL_BIGHA, FINAL_BISWA,FINAL_BISWASI = biswasiyan_to_bbb(total_area_biswasi)

        return [FINAL_BIGHA, FINAL_BISWA,FINAL_BISWASI]



    else:
        total_area_sarsahi = (value1*180) + (value2*9) + value3
        total_area_add_subtract = (value4*180) + (value5*9) + value6

        if add_or_subtract == 'Add':
            total_area_sarsahi = total_area_sarsahi + total_area_add_subtract
        else:
            total_area_sarsahi = total_area_sarsahi - total_area_add_subtract
        
        FINAL_KANAL, FINAL_MARLA,FINAL_SARSAHI = convert_sarsahi_to_kms(total_area_sarsahi)
        return[FINAL_KANAL, FINAL_MARLA,FINAL_SARSAHI]




# --------------------------------------------
# CONVERT BISWASIYAN TO BIGHA-BISWA-BISWASIYAN
# --------------------------------------------
def biswasiyan_to_bbb(INDIVIDUAL_SHARE_BISWASIYAN):
    # Step 2: Convert individual share to integer and fractional parts
    BISWASIYAN_ROUND = int(INDIVIDUAL_SHARE_BISWASIYAN)
    EXTRA_BISWASIYAN = INDIVIDUAL_SHARE_BISWASIYAN - BISWASIYAN_ROUND

    # Step 3: Convert biswasiyan to biswa
    BISWE_IN_ROUND_BISWASI = BISWASIYAN_ROUND / 20
    BISWE_ROUND = int(BISWE_IN_ROUND_BISWASI)
    EXTRA_BISWE = round(BISWE_IN_ROUND_BISWASI - BISWE_ROUND, 2)

    # Step 4: Convert biswa to bigha
    BIGHA_IN_ROUND_BISWA = BISWE_ROUND / 20
    BIGHA_ROUND = int(BIGHA_IN_ROUND_BISWA)
    EXTRA_BIGHA = round(BIGHA_IN_ROUND_BISWA - BIGHA_ROUND, 2)

    # Set FINAL_BIGHA value
    FINAL_BIGHA = BIGHA_ROUND

    # Convert EXTRA_BIGHA to BISWA
    BISWA_TO_ADD = EXTRA_BIGHA * 20
    EXTRA_BISWE += BISWA_TO_ADD

    # Handle cases where EXTRA_BISWE >= 20 or < 20
    if EXTRA_BISWE < 20:
        EXTRA_BISWE_ROUND = int(EXTRA_BISWE)
        FINAL_BISWA = EXTRA_BISWE_ROUND

        EXTRA_EXTRA_BISWE = EXTRA_BISWE - EXTRA_BISWE_ROUND
        BISWASIYAN_IN_EXTRA_EXTRA_BISWE = EXTRA_EXTRA_BISWE * 20
        EXTRA_BISWASIYAN += BISWASIYAN_IN_EXTRA_EXTRA_BISWE

        if EXTRA_BISWASIYAN < 20:
            FINAL_BISWASI = EXTRA_BISWASIYAN
        else:
            FINAL_BISWA += 1
            FINAL_BISWASI = EXTRA_BISWASIYAN - 20

    else:
        FINAL_BIGHA += 1
        EXTRA_BISWE -= 20
        EXTRA_EXTRA_BISWE_ROUND = int(EXTRA_BISWE)
        FINAL_BISWA = EXTRA_EXTRA_BISWE_ROUND
        REMAINING_BISWE = EXTRA_BISWE - EXTRA_EXTRA_BISWE_ROUND
        EXTRA_BISWASIYAN += REMAINING_BISWE * 20

        if EXTRA_BISWASIYAN < 20:
            FINAL_BISWASI = EXTRA_BISWASIYAN
        else:
            FINAL_BISWA += 1
            FINAL_BISWASI = EXTRA_BISWASIYAN - 20

    # Format the final result
    FINAL_BISWASI = round(FINAL_BISWASI, 2)

    # formatted_share = f"{FINAL_BIGHA}-{FINAL_BISWA}-{int(FINAL_BISWASI) if FINAL_BISWASI.is_integer() else FINAL_BISWASI:.2f}"
    return [FINAL_BIGHA, FINAL_BISWA,FINAL_BISWASI]



# --------------------------------------------
# CONVERT SARSAHIYAN TO KANAL-MARLA-SARSAHIYAN
# --------------------------------------------
def convert_sarsahi_to_kms(INDIVIDUAL_SHARE_SARSAHIYAN):
    # Step 2: Convert individual share to integer and fractional parts
    SARSAHIYAN_ROUND = int(INDIVIDUAL_SHARE_SARSAHIYAN)
    EXTRA_SARSAHIYAN = INDIVIDUAL_SHARE_SARSAHIYAN - SARSAHIYAN_ROUND

    # Step 3: Convert SARSAHIyan to MARLA
    MARLA_IN_ROUND_SARSAHI = SARSAHIYAN_ROUND / 9
    MARLA_ROUND = int(MARLA_IN_ROUND_SARSAHI)
    EXTRA_MARLA = round(MARLA_IN_ROUND_SARSAHI - MARLA_ROUND, 2)

    # Step 4: Convert MARLA to KANAL
    KANAL_IN_ROUND_MARLA = MARLA_ROUND / 20
    KANAL_ROUND = int(KANAL_IN_ROUND_MARLA)
    EXTRA_KANAL = round(KANAL_IN_ROUND_MARLA - KANAL_ROUND, 2)

    # Set FINAL_KANAL value
    FINAL_KANAL = KANAL_ROUND

    # Convert EXTRA_KANAL to MARLA
    MARLA_TO_ADD = EXTRA_KANAL * 20
    EXTRA_MARLA += MARLA_TO_ADD

    # Handle cases where EXTRA_MARLA >= 20 or < 20
    if EXTRA_MARLA < 20:
        EXTRA_MARLA_ROUND = int(EXTRA_MARLA)
        FINAL_MARLA = EXTRA_MARLA_ROUND

        EXTRA_EXTRA_MARLA = EXTRA_MARLA - EXTRA_MARLA_ROUND
        SARSAHIYAN_IN_EXTRA_EXTRA_MARLA = EXTRA_EXTRA_MARLA * 9
        EXTRA_SARSAHIYAN += SARSAHIYAN_IN_EXTRA_EXTRA_MARLA

        if EXTRA_SARSAHIYAN < 9:
            FINAL_SARSAHI = EXTRA_SARSAHIYAN
        else:
            FINAL_MARLA += 1
            FINAL_SARSAHI = EXTRA_SARSAHIYAN - 9

    else:
        FINAL_KANAL += 1
        EXTRA_MARLA -= 20
        EXTRA_EXTRA_MARLA_ROUND = int(EXTRA_MARLA)
        FINAL_MARLA = EXTRA_EXTRA_MARLA_ROUND
        REMAINING_MARLA = EXTRA_MARLA - EXTRA_EXTRA_MARLA_ROUND
        EXTRA_SARSAHIYAN += REMAINING_MARLA * 9

        if EXTRA_SARSAHIYAN < 9:
            FINAL_SARSAHI = EXTRA_SARSAHIYAN
        else:
            FINAL_MARLA += 1
            FINAL_SARSAHI = EXTRA_SARSAHIYAN - 9

    # Format the final result
    FINAL_SARSAHI = round(FINAL_SARSAHI, 3)

    # formatted_share = f"{FINAL_KANAL}-{FINAL_MARLA}-{int(FINAL_SARSAHI) if FINAL_SARSAHI.is_integer() else FINAL_SARSAHI:.2f}"
    return [FINAL_KANAL, FINAL_MARLA,FINAL_SARSAHI]