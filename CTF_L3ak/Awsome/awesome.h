/* Automatically generated by wasm2c */
#ifndef AWESOME_H_GENERATED_
#define AWESOME_H_GENERATED_

#include "wasm-rt.h"

#include <stdint.h>

#ifndef WASM_RT_CORE_TYPES_DEFINED
#define WASM_RT_CORE_TYPES_DEFINED
typedef uint8_t u8;
typedef int8_t s8;
typedef uint16_t u16;
typedef int16_t s16;
typedef uint32_t u32;
typedef int32_t s32;
typedef uint64_t u64;
typedef int64_t s64;
typedef float f32;
typedef double f64;
#endif

#ifdef __cplusplus
extern "C" {
#endif

typedef struct w2c_awesome__bg {
  u32 w2c_g0;
  wasm_rt_memory_t w2c_memory;
  wasm_rt_funcref_table_t w2c_T0;
} w2c_awesome__bg;

void wasm2c_awesome__bg_instantiate(w2c_awesome__bg*);
void wasm2c_awesome__bg_free(w2c_awesome__bg*);
wasm_rt_func_type_t wasm2c_awesome__bg_get_func_type(uint32_t param_count, uint32_t result_count, ...);

/* export: 'memory' */
wasm_rt_memory_t* w2c_awesome__bg_memory(w2c_awesome__bg* instance);

/* export: 'check' */
u32 w2c_awesome__bg_check(w2c_awesome__bg*, u32, u32);

/* export: '__wbindgen_malloc' */
u32 w2c_awesome__bg_0x5F_wbindgen_malloc(w2c_awesome__bg*, u32, u32);

/* export: '__wbindgen_realloc' */
u32 w2c_awesome__bg_0x5F_wbindgen_realloc(w2c_awesome__bg*, u32, u32, u32, u32);

#ifdef __cplusplus
}
#endif

#endif  /* AWESOME_H_GENERATED_ */