def format_duration(seconds):
    
    minute = seconds // 60
    hour = seconds // 3600
    day = seconds // 86400
    year = seconds // 31536000
    second = minute * 60 - seconds 
    print('{} Years, {} Days, {} Hours, {} Minutes, {} Seconds'.format(year,day,hour,minute,second))