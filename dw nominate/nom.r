nom_dat <- read_csv
("https://voteview.com/static/data/out/members/HSall_members.csv")

south <- c(40:49,51,53)
polar_dat <- nom_dat %>% 
    filter(congress>45 & 
           chamber != "President") %>%
    mutate( 
      year = 2*(congress-1) + 1789,
    ) %>%
    group_by(chamber,congress,year) %>% 
    summarize(
      party.mean.diff.d1 = mean(nominate_dim1[party_code==200],na.rm=T) - 
                           mean(nominate_dim1[party_code==100],na.rm=T),
      prop.moderate.d1 = mean(abs(nominate_dim1)<0.25,na.rm=T),
      prop.moderate.dem.d1 = mean(abs(nominate_dim1[party_code==100])<0.25,na.rm=T), # nolint
      prop.moderate.rep.d1 = mean(abs(nominate_dim1[party_code==200])<0.25,na.rm=T), # nolint
      overlap = (sum(nominate_dim1[party_code==200] < # nolint
                       max(nominate_dim1[party_code==100],na.rm=T),na.rm=T)  +
                 sum(nominate_dim1[party_code==100] >
                       min(nominate_dim1[party_code==200],na.rm=T),na.rm=T))/
                 (sum(!is.na(nominate_dim1[party_code==100]))+
                  sum(!is.na(nominate_dim1[party_code==200]))),
      chamber.mean.d1 = mean(nominate_dim1,na.rm=T),
      chamber.mean.d2 = mean(nominate_dim2,na.rm=T),
      dem.mean.d1 = mean(nominate_dim1[party_code==100],na.rm=T),
      dem.mean.d2 = mean(nominate_dim2[party_code==100],na.rm=T),
      rep.mean.d1 = mean(nominate_dim1[party_code==200],na.rm=T),
      rep.mean.d2 = mean(nominate_dim2[party_code==200],na.rm=T),
      north.rep.mean.d1 = mean(nominate_dim1[party_code==200 & 
                                             !(state_icpsr %in% south)],na.rm=T),    
      north.rep.mean.d2 = mean(nominate_dim2[party_code==200 & 
                                             !(state_icpsr %in% south)],na.rm=T),    
      south.rep.mean.d1 = mean(nominate_dim1[party_code==200 & 
                                              (state_icpsr %in% south)],na.rm=T),    
      south.rep.mean.d2 = mean(nominate_dim2[party_code==200 & 
                                             (state_icpsr %in% south)],na.rm=T),    
      north.dem.mean.d1 = mean(nominate_dim1[party_code==100 & 
                                              !(state_icpsr %in% south)],na.rm=T),    
      north.dem.mean.d2 = mean(nominate_dim2[party_code==100 & 
                                              !(state_icpsr %in% south)],na.rm=T),    
      south.dem.mean.d1 = mean(nominate_dim1[party_code==100 & 
                                              (state_icpsr %in% south)],na.rm=T),    
      south.dem.mean.d2 = mean(nominate_dim2[party_code==100 & 
                                              (state_icpsr %in% south)],na.rm=T),    
    )

