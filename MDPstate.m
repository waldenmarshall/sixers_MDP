classdef MDPstate
    properties (SetAccess = protected)
      cur_score (1,1) uint8 {mustBeInteger, mustBeNonnegative,...
          mustBeLessThanOrEqual(cur_score, 36)} ...
          =cast(0,'uint8')%sum of dice kept
      dice (:,1) uint8 {mustBeInteger, mustBeNonnegative,...
          mustBeLessThanOrEqual(dice, 6)} ...
          =cast(zeros(6,1),'uint8')%ordered multiset of dice in play
    end
   methods
       function self = MDPstate(cur_score, dice)
           %constructor for looping creating entire single player state
           self.cur_score = cur_score;
           self.dice =  dice;
       end
   end
end