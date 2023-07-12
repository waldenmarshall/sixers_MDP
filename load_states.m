function states = load_states(filename)
    buf=importfile(filename);
    states = cell(length(buf)+1,1);
    states{1} = [];

    for i = 1:length(buf)
        state = buf(i,:);
        states{i+1} = rmmissing(state);
    end
end