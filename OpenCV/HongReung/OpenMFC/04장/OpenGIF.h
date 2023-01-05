// OpenGIF.h: interface for the COpenGIF class.
//
//////////////////////////////////////////////////////////////////////

#if !defined(AFX_OPENGIF_H__80654250_7F2D_4E34_8737_DBE78AD9620F__INCLUDED_)
#define AFX_OPENGIF_H__80654250_7F2D_4E34_8737_DBE78AD9620F__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

class COpenGIF  
{
public:
	COpenGIF();
	virtual ~COpenGIF();

#ifndef TRUE
#define TRUE 1
#endif
#ifndef FALSE
#define FALSE 0
#endif

/* define constants and defaults */
    /* Default amount of inter-frame time */
#define DEFAULT_TIME 10
    /* If set to 1, Netscape 'loop' code will be added by default */
#define DEFAULT_LOOP 0
    /* If set to 1, use the colormaps from all images, not just the first */
#define DEFAULT_USE_COLORMAP 0

    /* Used in calculating the transparent color */
#define TRANS_NONE 1
#define TRANS_RGB 2
#define TRANS_MAP 3

#define DISP_NONE 0
#define DISP_NOT  1
#define DISP_BACK 2
#define DISP_PREV 3
#define DEFAULT_DISPOSAL DISP_NONE
    /* set default disposal method here to any of the DISP_XXXX values */

#define BIGSTRING 256
#define MAXVAL  4096        /* maxval of lzw coding size */
#define MAXVALP 4096
#define TERMIN 'T'
#define LOOKUP 'L'
#define SEARCH 'S'
#define noOfArrays 20
/* defines the amount of memory set aside in the encoding for the
 * LOOKUP type nodes; for a 256 color GIF, the number of LOOKUP
 * nodes will be <= noOfArrays, for a 128 color GIF the number of
 * LOOKUP nodes will be <= 2 * noOfArrays, etc.  */

/* define shorthand for various types */
#define LONG int
#define ULONG unsigned int
#define BYTE char
#define UBYTE unsigned char
#define SHORT short
#define USHORT unsigned short
#define WORD short int
#define UWORD unsigned short int


/* definition of various structures */
typedef struct Transparency {
  int type;
  UBYTE valid;
  UBYTE map;
  UBYTE red;
  UBYTE green;
  UBYTE blue;
  } Transparency;

typedef struct Global {
  Transparency trans;
  int left;
  int top;
  unsigned int time;
  unsigned short disposal;
  } Global;

typedef struct GifScreenHdr {
  int width;
  int height;
  UBYTE m;
  UBYTE cres;
  UBYTE pixbits;
  UBYTE bc;
  UBYTE aspect;
 } GifScreenHdr;

typedef union GifColor {
  struct cmap {
    UBYTE red;
    UBYTE green;
    UBYTE blue;
    UBYTE pad;
   } cmap;
  ULONG pixel;
 } GifColor;

typedef struct GifImageHdr {
  int left;
  int top;
  int width;
  int height;
  UBYTE m;
  UBYTE i;
  UBYTE pixbits;
  UBYTE reserved;
 } GifImageHdr;

typedef struct GifTree {
  char typ;             /* terminating, lookup, or search */
  int code;             /* the code to be output */
  UBYTE ix;             /* the color map index */
  struct GifTree **node, *nxt, *alt;
} GifTree;

/* define inline functions */
#define GifPutShort(i, fout)    {fputc(i&0xff, fout); fputc(i>>8, fout);}
#define GifGetShort(fin)        (Xgetc(fin) | Xgetc(fin)<<8)


	/* forward declaration of the functions  */
	char *AddCodeToBuffer(int, short, char *);
	void ClearTree(int, GifTree *);
	void GifClearTable();
	UBYTE *GifSendData(UBYTE *, int, UBYTE *);
	void SetOffset(char *);
	UBYTE Xgetc(FILE *fin);


	// loadGIF
	// Loads an image from a GIF file
	//
	IplImage *loadGIF (const char *name);
	//    name
	//        Name of the file to be loaded.
	//
	// The function loadGIF loads an image from the specified GIF file
	// and returns the pointer to the loaded image. If the image cannot be
	// loaded, it returns NULL. Otherwise, the image has always 3 channels
	// (i.e. the palette is applied, even though the palette is grayscale).
	// GIF87a and GIF89a are supported. If the file contains an animated
	// GIF, the first frame of the file is loaded.


	// saveGIF
	// Saves an image to a GIF file
	//
	int saveGIF (const char *name, IplImage *img);
	//    name
	//        Name of the file to be saved.
	//    img
	//        Image to be saved.
	//
	// The function saveGIF saves the image to the specified GIF file.
	// Only 8U-bit single-channel or 3-channel (with 'BGR' channel order)
	// images can be saved using this function. In the first case, a
	// grayscale palette is used. In the second case, a fixed palette is
	// used, with 3 bits for red, 3 bits for green, and 2 bits for blue.
	// A simple dithering algorithm is applied. On error, the function
	// returns 0, otherwise 1.
};

#endif // !defined(AFX_OPENGIF_H__80654250_7F2D_4E34_8737_DBE78AD9620F__INCLUDED_)
