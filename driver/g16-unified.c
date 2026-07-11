/* Grok16 unified driver stub — HARD 16.1.0
 * Full driver links via field_opt; this unit asserts hard defines.
 */
#ifndef G16_HARD
#define G16_HARD 1
#endif
#ifndef G16_NO_EXPLOIT
#define G16_NO_EXPLOIT 1
#endif
#ifndef NO_SOFT_KILL
#define NO_SOFT_KILL 1
#endif

int g16_hard_version(void) {
  return 16100; /* 16.1.0-hard */
}

int g16_exploits_dispermitted(void) {
  return 1;
}
