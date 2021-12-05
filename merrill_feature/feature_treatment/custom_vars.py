#


#


#


#


#
def custom_vars_202105rates(data_pct):

    # relative stocks
    data_pct['SPA_CN_to_US'] = data_pct['SPASTT01CNM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_IN_to_US'] = data_pct['SPASTT01INM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_EZ_to_US'] = data_pct['SPASTT01EZM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_GB_to_US'] = data_pct['SPASTT01GBM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_DE_to_US'] = data_pct['SPASTT01DEM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_KR_to_US'] = data_pct['SPASTT01KRM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_TR_to_US'] = data_pct['SPASTT01TRM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_MX_to_US'] = data_pct['SPASTT01MXM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_BR_to_US'] = data_pct['SPASTT01BRM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_RU_to_US'] = data_pct['SPASTT01RUM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_AU_to_US'] = data_pct['SPASTT01AUM657N'] - data_pct['SPASTT01USM657N']
    data_pct['SPA_ZA_to_US'] = data_pct['SPASTT01ZAM657N'] - data_pct['SPASTT01USM657N']

    # spreads
    data_pct['GS1M_m_GS20'] = data_pct['GS1M'] - data_pct['GS20']
    data_pct['GS3M_m_GS20'] = data_pct['GS3M'] - data_pct['GS20']
    data_pct['GS1_m_GS20'] = data_pct['GS1'] - data_pct['GS20']
    data_pct['GS2_m_GS20'] = data_pct['GS2'] - data_pct['GS20']
    data_pct['GS3_m_GS20'] = data_pct['GS3'] - data_pct['GS20']
    data_pct['GS10_m_GS20'] = data_pct['GS10'] - data_pct['GS20']
    data_pct['FED_m_GS20'] = data_pct['FEDFUNDS'] - data_pct['GS20']

    # interest rates relative to us
    data_pct['BR_m_US'] = data_pct['INTDSRBRM193N'] - data_pct['INTDSRUSM193N']
    data_pct['TR_m_US'] = data_pct['INTDSRTRM193N'] - data_pct['INTDSRUSM193N']
    data_pct['IN_m_US'] = data_pct['INTDSRINM193N'] - data_pct['INTDSRUSM193N']
    data_pct['CN_m_US'] = data_pct['INTDSRCNM193N'] - data_pct['INTDSRUSM193N']

    # us stocks minus balance of payments
    data_pct['US_S_m_BoP'] = data_pct['SPASTT01USM657N'] - data_pct['BOPGSTB']

    # us stocks minus saving rate
    data_pct['US_S_m_PSR'] = data_pct['SPASTT01USM657N'] - data_pct['PSAVERT']

    # us stocks minus real estate
    data_pct['US_S_m_RE'] = data_pct['SPASTT01USM657N'] - data_pct['JTU5300QUL']

    # 1Y yields minus inflation expectations
    data_pct['GS1_m_MICH'] = data_pct['GS1'] - data_pct['MICH']

    # commercial papers minus stocks
    data_pct['US_S_m_PSR'] = data_pct['SPASTT01USM657N'] - data_pct['DTBSPCKFM']

    # small time deposits minus stocks
    data_pct['US_S_m_SMTDE'] = data_pct['SPASTT01USM657N'] - data_pct['STDSL']

    # AAA minus BAA spread
    data_pct['AAA_m_BAA'] = data_pct['AAA'] - data_pct['BAA']

    # PPI minus CPI
    data_pct['PPI_m_CPI'] = data_pct['PCUOMFGOMFG'] - data_pct['CPIAUCSL']

    # PPI minus unemployment
    data_pct['PPI_m_UNEMPL'] = data_pct['PCUOMFGOMFG'] - data_pct['UNRATE']

    # PPI minus Employment-Population Ratio
    data_pct['PPI_m_EMPLRA'] = data_pct['PCUOMFGOMFG'] - data_pct['EMRATIO']

    # Savings to Total Employed
    data_pct['SAV_to_TOTAEMPL'] = (1 + data_pct['PMSAVE']) / (1 + data_pct['CE16OV']) - 1
    data_pct.loc[data_pct['CE16OV'] == 0, 'SAV_to_TOTAEMPL'] = 0
    # Savings to Manu Employed
    data_pct['SAV_to_MANUEMPL'] = (1 + data_pct['PMSAVE']) / (1 + data_pct['MANEMP']) - 1
    data_pct.loc[data_pct['MANEMP'] == 0, 'SAV_to_MANUEMPL'] = 0
    # Consumption to Total Employed
    # data_pct['CONS_to_TOTAEMPL'] = data_pct['PCEC96'] / data_pct['CE16OV']
    # Consumption to Manu Employed
    # data_pct['CONS_to_MANUEMPL'] = data_pct['PCEC96'] / data_pct['MANEMP']

    # Hourly Earnings X Hours
    data_pct['HE_X_HOURS'] = (1 + data_pct['CES3000000008']) * (1 + data_pct['AWHMAN']) - 1

    return data_pct


def custom_vars_202105qe(data_pct):
    # QE activities status
    data_pct['WORAL_ACTIVE'] = (data_pct['WORAL'] > 0).astype(dtype=float) * 2 - 1
    data_pct['WORAL_sum_ACTIVE'] = (data_pct['WORAL_sum'] > 0).astype(dtype=float) * 2 - 1
    data_pct['RESPPANWW_ACTIVE'] = (data_pct['RESPPANWW'] > 0).astype(dtype=float) * 2 - 1
    return data_pct
