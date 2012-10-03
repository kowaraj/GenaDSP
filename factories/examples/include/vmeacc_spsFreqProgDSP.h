// VME accessors .h for spsFreqProgDSP
// Generated from: spsFreqProgDSP.xml, 
//           memory map version: 20120718
// Generated on: 2012-10-03 10:23:01,
//           by: kowaraj,
//           using: GenaDSP (v2012-10-02)
// 

unsigned int get_dspVersion(void);
void set_dspVersion(unsigned int val);

unsigned int get_dspSubVersion(void);
void set_dspSubVersion(unsigned int val);

unsigned int get_dspStatus(void);
void set_dspStatus(unsigned int val);

unsigned int get_dspStatus_dspDone(void);
// read-only: dspStatus_dspDone

unsigned int get_dspStatus_dspRun(void);
// read-only: dspStatus_dspRun

unsigned int get_dspStatus_rephMode(void);
// read-only: dspStatus_rephMode

// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
unsigned int get_dspFaults(void);
void set_dspFaults(unsigned int val);

unsigned int get_dspFaults_spare(void);
// read-only: dspFaults_spare

unsigned int get_control2(void);
// read-only: control2

unsigned int get_control2_enaRadialSteering(void);
// read-only: control2_enaRadialSteering

unsigned int get_control2_enaPlayback(void);
// read-only: control2_enaPlayback

unsigned int get_control2_enaRecord(void);
// read-only: control2_enaRecord

unsigned int get_control3(void);
// read-only: control3

unsigned int get_control3_dspTask(void);
// read-only: control3_dspTask

unsigned int get_control3_rephMode(void);
// read-only: control3_rephMode

// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
float get_rephDataIn(void);
// read-only: rephDataIn

float get_rephParamB0(void);
// read-only: rephParamB0

float get_rephParamMq(void);
// read-only: rephParamMq

float get_rephParamGTrans(void);
// read-only: rephParamGTrans

float get_rephConstMaxSlope(void);
// read-only: rephConstMaxSlope

float get_rephConstSPSRad(void);
// read-only: rephConstSPSRad

unsigned int get_rephConstFInf(void);
// read-only: rephConstFInf

unsigned int get_udCounter(void);
// read-only: udCounter

unsigned int get_radialSteering(void);
// read-only: radialSteering

unsigned int get_coarseFP(void);
void set_coarseFP(unsigned int val);

unsigned int get_ddsFTW1(void);
void set_ddsFTW1(unsigned int val);

unsigned int get_ddsFTW2(void);
void set_ddsFTW2(unsigned int val);

unsigned int get_dbgIrq0Cnt(void);
void set_dbgIrq0Cnt(unsigned int val);

unsigned int get_dbgIrq1Cnt(void);
void set_dbgIrq1Cnt(unsigned int val);

