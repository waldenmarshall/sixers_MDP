function p = prob_roll(dice)
    sz = length(dice);
    dice = reshape(dice, [length(dice),1]);
    num_seq = 6^sz; %number of ordered of size equal to the state of interest
    [GC, ~] = groupcounts(dice); %GC is the multiplicities of elements
    num_perm = multinomial_coefficient(GC);
    p = num_perm/num_seq;
end