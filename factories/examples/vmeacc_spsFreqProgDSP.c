// VME accessors .c for spsFreqProgDSP
// Generated from: spsFreqProgDSP.xml, 
//           memory map version: 20120718
// Generated on: 2012-10-03 10:23:01,
//           by: kowaraj,
//           using: GenaDSP (v2012-10-02)
// 

#include "include\MemMapDSP_spsFreqProgDSP.h"

unsigned int get_dspVersion() {
	unsigned int* preg = (unsigned int*)dspVersion;
	return (unsigned int) *preg;
}
void set_dspVersion(unsigned int val) {
	unsigned int* preg = (unsigned int*)dspVersion;
	*preg = val;
}

unsigned int get_dspSubVersion() {
	unsigned int* preg = (unsigned int*)dspSubVersion;
	return (unsigned int) *preg;
}
void set_dspSubVersion(unsigned int val) {
	unsigned int* preg = (unsigned int*)dspSubVersion;
	*preg = val;
}

unsigned int get_dspStatus() {
	unsigned int* preg = (unsigned int*)dspStatus;
	return (unsigned int) *preg;
}
void set_dspStatus(unsigned int val) {
	unsigned int* preg = (unsigned int*)dspStatus;
	*preg = val;
}

unsigned int get_dspStatus_dspDone() {
	unsigned int* preg = (unsigned int*)dspStatus_dspDone;
	unsigned int bmask = 0x00000040;
	unsigned int b_lsb = 6;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: dspStatus_dspDone

unsigned int get_dspStatus_dspRun() {
	unsigned int* preg = (unsigned int*)dspStatus_dspRun;
	unsigned int bmask = 0x00000080;
	unsigned int b_lsb = 7;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: dspStatus_dspRun

unsigned int get_dspStatus_rephMode() {
	unsigned int* preg = (unsigned int*)dspStatus_rephMode;
	unsigned int bmask = 0x0000000F;
	unsigned int b_lsb = 0;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: dspStatus_rephMode

// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
unsigned int get_dspFaults() {
	unsigned int* preg = (unsigned int*)dspFaults;
	return (unsigned int) *preg;
}
void set_dspFaults(unsigned int val) {
	unsigned int* preg = (unsigned int*)dspFaults;
	*preg = val;
}

unsigned int get_dspFaults_spare() {
	unsigned int* preg = (unsigned int*)dspFaults_spare;
	unsigned int bmask = 0x00000080;
	unsigned int b_lsb = 7;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: dspFaults_spare

unsigned int get_control2() {
	unsigned int* preg = (unsigned int*)control2;
	return (unsigned int) *preg;
}
// read-only: control2

unsigned int get_control2_enaRadialSteering() {
	unsigned int* preg = (unsigned int*)control2_enaRadialSteering;
	unsigned int bmask = 0x00000001;
	unsigned int b_lsb = 0;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: control2_enaRadialSteering

unsigned int get_control2_enaPlayback() {
	unsigned int* preg = (unsigned int*)control2_enaPlayback;
	unsigned int bmask = 0x00000002;
	unsigned int b_lsb = 1;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: control2_enaPlayback

unsigned int get_control2_enaRecord() {
	unsigned int* preg = (unsigned int*)control2_enaRecord;
	unsigned int bmask = 0x00000004;
	unsigned int b_lsb = 2;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: control2_enaRecord

unsigned int get_control3() {
	unsigned int* preg = (unsigned int*)control3;
	return (unsigned int) *preg;
}
// read-only: control3

unsigned int get_control3_dspTask() {
	unsigned int* preg = (unsigned int*)control3_dspTask;
	unsigned int bmask = 0x00000080;
	unsigned int b_lsb = 7;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: control3_dspTask

unsigned int get_control3_rephMode() {
	unsigned int* preg = (unsigned int*)control3_rephMode;
	unsigned int bmask = 0x0000000F;
	unsigned int b_lsb = 0;
	unsigned int bval = ( (*preg & bmask) >> b_lsb );
	return bval;
}
// read-only: control3_rephMode

// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
// Not implemented yet: no code-field getter
float get_rephDataIn() {
	float* preg = (float*)rephDataIn;
	return (float) *preg;
}
// read-only: rephDataIn

float get_rephParamB0() {
	float* preg = (float*)rephParamB0;
	return (float) *preg;
}
// read-only: rephParamB0

float get_rephParamMq() {
	float* preg = (float*)rephParamMq;
	return (float) *preg;
}
// read-only: rephParamMq

float get_rephParamGTrans() {
	float* preg = (float*)rephParamGTrans;
	return (float) *preg;
}
// read-only: rephParamGTrans

float get_rephConstMaxSlope() {
	float* preg = (float*)rephConstMaxSlope;
	return (float) *preg;
}
// read-only: rephConstMaxSlope

float get_rephConstSPSRad() {
	float* preg = (float*)rephConstSPSRad;
	return (float) *preg;
}
// read-only: rephConstSPSRad

unsigned int get_rephConstFInf() {
	unsigned int* preg = (unsigned int*)rephConstFInf;
	return (unsigned int) *preg;
}
// read-only: rephConstFInf

unsigned int get_udCounter() {
	unsigned int* preg = (unsigned int*)udCounter;
	return (unsigned int) *preg;
}
// read-only: udCounter

unsigned int get_radialSteering() {
	unsigned int* preg = (unsigned int*)radialSteering;
	return (unsigned int) *preg;
}
// read-only: radialSteering

unsigned int get_coarseFP() {
	unsigned int* preg = (unsigned int*)coarseFP;
	return (unsigned int) *preg;
}
void set_coarseFP(unsigned int val) {
	unsigned int* preg = (unsigned int*)coarseFP;
	*preg = val;
}

unsigned int get_ddsFTW1() {
	unsigned int* preg = (unsigned int*)ddsFTW1;
	return (unsigned int) *preg;
}
void set_ddsFTW1(unsigned int val) {
	unsigned int* preg = (unsigned int*)ddsFTW1;
	*preg = val;
}

unsigned int get_ddsFTW2() {
	unsigned int* preg = (unsigned int*)ddsFTW2;
	return (unsigned int) *preg;
}
void set_ddsFTW2(unsigned int val) {
	unsigned int* preg = (unsigned int*)ddsFTW2;
	*preg = val;
}

unsigned int get_dbgIrq0Cnt() {
	unsigned int* preg = (unsigned int*)dbgIrq0Cnt;
	return (unsigned int) *preg;
}
void set_dbgIrq0Cnt(unsigned int val) {
	unsigned int* preg = (unsigned int*)dbgIrq0Cnt;
	*preg = val;
}

unsigned int get_dbgIrq1Cnt() {
	unsigned int* preg = (unsigned int*)dbgIrq1Cnt;
	return (unsigned int) *preg;
}
void set_dbgIrq1Cnt(unsigned int val) {
	unsigned int* preg = (unsigned int*)dbgIrq1Cnt;
	*preg = val;
}

