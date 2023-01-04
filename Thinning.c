void Thinning(Mat input, int row, int col)
{
    int x, y, p, q, xp, yp, xm, ym, cc, cd;
    int np1, sp1, hv;
    int cnt=0, chk=0, flag=0;
 
    unsigned char *m_BufImage;
    unsigned char *m_ResultImg;
    m_BufImage =    (unsigned char*)malloc(sizeof(unsigned char)*row*col);
    m_ResultImg =    (unsigned char*)malloc(sizeof(unsigned char)*row*col);
 
    // Result image에 Mat format의 input image Copy
    for( y = 0 ; y < row ; y ++ ){
        for( x = 0 ; x < col ; x++ ){
            *(m_ResultImg+(col*y)+x) = input.at<uchar>(y,x);
        }
    }
 
    do{
        // Image Buffer를 0으로 셋팅
        for( y = 1 ; y < row-1 ; y ++ ){
            for( x = 1 ; x < col-1 ; x++ ){
                *(m_BufImage+(col*y)+x) = 0;
            }
        }
 
        // 천이 추출
        if(chk == 0) flag = 0;
        chk = cnt % 2;
        cnt ++;
 
        for( y = 1 ; y < row-1 ; y ++ ){
            ym = y - 1;
            yp = y + 1;
            for( x = 1 ; x < col-1 ; x ++ ){
                if(*(m_ResultImg+(col*y)+x) == 0) continue;
 
                np1 = 0;
                for(q = y-1 ; q <= y+1; q ++ ){
                    for(p = x-1 ; p <= x+1; p ++ ){
                        if(*(m_ResultImg+(col*q)+p) != 0) np1++;
                    }
                }
 
                if(np1 < 3 || np1 > 7){
                    *(m_BufImage+(col*y)+x) = 255;
                    continue;                    
                }
 
                xm = x - 1;
                xp = x + 1;
                sp1 = 0;
 
                if(*(m_ResultImg+(col*ym)+x) == 0 && *(m_ResultImg+(col*ym)+xp) != 0) sp1++;
                if(*(m_ResultImg+(col*ym)+xp) == 0 && *(m_ResultImg+(col*y)+xp) != 0) sp1++;
                if(*(m_ResultImg+(col*y)+xp) == 0 && *(m_ResultImg+(col*yp)+xp) != 0) sp1++;
                if(*(m_ResultImg+(col*yp)+xp) == 0 && *(m_ResultImg+(col*yp)+x) != 0) sp1++;
                if(*(m_ResultImg+(col*yp)+x) == 0 && *(m_ResultImg+(col*yp)+xm) != 0) sp1++;
                if(*(m_ResultImg+(col*yp)+xm) == 0 && *(m_ResultImg+(col*y)+xm) != 0) sp1++;
                if(*(m_ResultImg+(col*y)+xm) == 0 && *(m_ResultImg+(col*ym)+xm) != 0) sp1++;
                if(*(m_ResultImg+(col*ym)+xm) == 0 && *(m_ResultImg+(col*ym)+x) != 0) sp1++;
 
                if(sp1 != 1){
                    *(m_BufImage+(col*y)+x) = 255;
                    continue;
                }
 
                if(chk == 0){
                    cc = *(m_ResultImg+(col*ym)+x) * *(m_ResultImg+(col*y)+xp);
                    cc = cc * *(m_ResultImg+(col*yp)+x);
 
                    cd = *(m_ResultImg+(col*y)+xp) * *(m_ResultImg+(col*yp)+x);
                    cd = cd * *(m_ResultImg+(col*y)+xm);
                }
                else{
                    cc = *(m_ResultImg+(col*ym)+x) * *(m_ResultImg+(col*y)+xp);
                    cc = cc * *(m_ResultImg+(col*y)+xm);
 
                    cd = *(m_ResultImg+(col*ym)+x) * *(m_ResultImg+(col*yp)+x);
                    cd = cd * *(m_ResultImg+(col*y)+xm);                
                }
 
                if(cc != 0 || cd != 0){
                    *(m_BufImage+(col*y)+x) = 255;
                    continue;
                }
                flag = 1;
            }
        }
 
        for( y = 1 ; y < row-1 ; y ++ ){
            for( x = 1 ; x < col-1 ; x ++ ){
                *(m_ResultImg+(col*y)+x) = *(m_BufImage+(col*y)+x);
            }
        }
    }while(!(chk == 1 && flag == 0));
 
    // 4연결점 처리
    for( y = 1 ; y < row-1 ; y ++ ){
        yp = y + 1;
        ym = y - 1;
        for( x = 1 ; x < col-1 ; x ++ ){
            if(*(m_ResultImg+(col*y)+x) == 0) continue;
 
            xm = x - 1;
            xp = x + 1;
            sp1 = 0;
            if(*(m_ResultImg+(col*ym)+x) == 0 && *(m_ResultImg+(col*ym)+xp) != 0) sp1++;
            if(*(m_ResultImg+(col*ym)+xp) == 0 && *(m_ResultImg+(col*y)+xp) != 0) sp1++;
            if(*(m_ResultImg+(col*y)+xp) == 0 && *(m_ResultImg+(col*yp)+xp) != 0) sp1++;
            if(*(m_ResultImg+(col*yp)+xp) == 0 && *(m_ResultImg+(col*yp)+x) != 0) sp1++;
            if(*(m_ResultImg+(col*yp)+x) == 0 && *(m_ResultImg+(col*yp)+xm) != 0) sp1++;
            if(*(m_ResultImg+(col*yp)+xm) == 0 && *(m_ResultImg+(col*y)+xm) != 0) sp1++;
            if(*(m_ResultImg+(col*y)+xm) == 0 && *(m_ResultImg+(col*ym)+xm) != 0) sp1++;
            if(*(m_ResultImg+(col*ym)+xm) == 0 && *(m_ResultImg+(col*ym)+x) != 0) sp1++;
 
            hv = 0;
            if(sp1 == 2){
                if        ((*(m_ResultImg+(col*ym)+x) & *(m_ResultImg+(col*y)+xp)) != 0) hv++;
                else if    ((*(m_ResultImg+(col*y)+xp) & *(m_ResultImg+(col*yp)+x)) != 0) hv++;
                else if    ((*(m_ResultImg+(col*yp)+x) & *(m_ResultImg+(col*y)+xm)) != 0) hv++;
                else if    ((*(m_ResultImg+(col*y)+xm) & *(m_ResultImg+(col*ym)+x)) != 0) hv++;
 
                if(hv == 1) *(m_ResultImg+(col*y)+x) = 0;
            }
            else if(sp1 == 3){
                if        ((*(m_ResultImg+(col*ym)+x) & *(m_ResultImg+(col*y)+xm) & *(m_ResultImg+(col*y)+xp)) != 0) hv++;
                else if    ((*(m_ResultImg+(col*yp)+x) & *(m_ResultImg+(col*y)+xm) & *(m_ResultImg+(col*y)+xp)) != 0) hv++;
                else if ((*(m_ResultImg+(col*ym)+x) & *(m_ResultImg+(col*yp)+x) & *(m_ResultImg+(col*y)+xm)) != 0) hv++;
                else if ((*(m_ResultImg+(col*ym)+x) & *(m_ResultImg+(col*yp)+x) & *(m_ResultImg+(col*y)+xp)) != 0) hv++;
 
                if(hv == 1) *(m_ResultImg+(col*y)+x) = 0;
            }
        }
    }
 
    // 들어온 배열에 재복사
    for( y = 0 ; y < row ; y ++ ){
        for( x = 0 ; x < col ; x++ ){
            input.at<uchar>(y,x) = *(m_ResultImg+(col*y)+x);
        }
    }
 
    free(m_BufImage);
    free(m_ResultImg);
}