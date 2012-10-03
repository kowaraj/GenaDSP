// DSP Memory map for spsFreqProgDSP
// Generated from: spsFreqProgDSP.xml, 
//           memory map version: 20120718
// Generated on: 2012-10-03 10:23:01,
//           by: kowaraj,
//           using: GenaDSP (v2012-10-02)
// 

#define DSP_VERSION 0x12100323 // format: 0xyymmddMM

#define dspVersion                     (0x00000000)// register-data, rw , unsigned int
#define dspSubVersion                  (0x00000004)// register-data, rw , unsigned int
#define dspStatus                      (0x00000008)// register-data, rw , unsigned int
#define dspStatus_dspDone              (0x00000040) // bit-field-data
#define dspStatus_dspRun               (0x00000080) // bit-field-data
#define dspStatus_rephMode             (0x0000000F) // sub-reg
#define dspStatus_rephMode_idle        0 // code-field
#define dspStatus_rephMode_fbottom     1 // code-field
#define dspStatus_rephMode_ramp        2 // code-field
#define dspStatus_rephMode_ftop        3 // code-field
#define dspStatus_rephMode_setfreq     4 // code-field
#define dspStatus_rephMode_coarse      5 // code-field
#define dspStatus_rephMode_pll         6 // code-field
#define dspStatus_rephMode_spare1      7 // code-field
#define dspFaults                      (0x0000000C)// register-data, rw , unsigned int
#define dspFaults_spare                (0x00000080) // bit-field-data
#define control2                       (0x00000010)// register-data, r  , unsigned int
#define control2_enaRadialSteering     (0x00000001) // bit-field-data
#define control2_enaPlayback           (0x00000002) // bit-field-data
#define control2_enaRecord             (0x00000004) // bit-field-data
#define control3                       (0x00000014)// register-data, r  , unsigned int
#define control3_dspTask               (0x00000080) // bit-field-data
#define control3_rephMode              (0x0000000F) // sub-reg
#define control3_rephMode_idle         0 // code-field
#define control3_rephMode_fbottom      1 // code-field
#define control3_rephMode_ramp         2 // code-field
#define control3_rephMode_ftop         3 // code-field
#define control3_rephMode_setfreq      4 // code-field
#define control3_rephMode_coarse       5 // code-field
#define control3_rephMode_pll          6 // code-field
#define control3_rephMode_spare1       8 // code-field
#define rephDataIn                     (0x00000018)// register-data, r  , float
#define rephParamB0                    (0x0000001C)// register-data, r  , float
#define rephParamMq                    (0x00000020)// register-data, r  , float
#define rephParamGTrans                (0x00000024)// register-data, r  , float
#define rephConstMaxSlope              (0x00000028)// register-data, r  , float
#define rephConstSPSRad                (0x0000002C)// register-data, r  , float
#define rephConstFInf                  (0x00000030)// register-data, r  , unsigned int
#define udCounter                      (0x00000034)// register-data, r  , unsigned int
#define radialSteering                 (0x00000038)// register-data, r  , unsigned int
#define coarseFP                       (0x0000003C)// register-data, w  , unsigned int
#define ddsFTW1                        (0x00000040)// register-data, w  , unsigned int
#define ddsFTW2                        (0x00000044)// register-data, rw , unsigned int
#define dbgIrq0Cnt                     (0x00000048)// register-data, rw , unsigned int
#define dbgIrq1Cnt                     (0x0000004C)// register-data, rw , unsigned int
